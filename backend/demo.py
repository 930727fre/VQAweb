import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_chroma import Chroma
import logging
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Tuple
from langchain_core.documents import Document
import os
from datetime import datetime
import json
from urllib.parse import urlparse
from langchain.prompts import PromptTemplate

PERSIST_DIRECTORY = "./vectorstore_db"
PROCESSING_LOG_FILE = "processed_urls.json"

# Define the generation prompt template
GENERATION_PROMPT = """Based on the following contexts, please provide a comprehensive answer to the question. 
Include relevant information from the contexts and synthesize it into a coherent response if the query is not relevant to what has retrieved, skip the retrieval data.

Question: {question}

Relevant contexts:
{contexts}

Answer:"""

class WebLoader:
    def __init__(self, urls: List[str]):
        self.urls = urls if isinstance(urls, list) else [urls]
        self.processing_log_path = os.path.join(PERSIST_DIRECTORY, PROCESSING_LOG_FILE)
        
    def _load_processing_log(self) -> Dict:
        if os.path.exists(self.processing_log_path):
            with open(self.processing_log_path, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_processing_log(self, log: Dict):
        os.makedirs(PERSIST_DIRECTORY, exist_ok=True)
        with open(self.processing_log_path, 'w') as f:
            json.dump(log, f, indent=2)
    
    def _process_url(self, url: str) -> Tuple[Document, bool]:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else urlparse(url).path
            content_tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            text = '\n\n'.join([tag.get_text(strip=True) for tag in content_tags if tag.get_text(strip=True)])
            
            if not text.strip():
                return None, False
            
            metadata = {
                "source": url,
                "title": title,
                "date_processed": datetime.now().isoformat()
            }
            
            return Document(page_content=text, metadata=metadata), True
            
        except Exception as e:
            print(f"Error processing URL {url}: {str(e)}")
            return None, False
    
    def load(self) -> List[Document]:
        processing_log = self._load_processing_log()
        documents = []
        
        for url in self.urls:
            if url in processing_log and processing_log[url]["success"]:
                print(f"Skipping previously processed URL: {url}")
                continue
                
            print(f"Processing URL: {url}")
            doc, success = self._process_url(url)
            
            if success and doc:
                documents.append(doc)
                processing_log[url] = {
                    "success": True,
                    "date_processed": datetime.now().isoformat(),
                    "title": doc.metadata.get("title", "Unknown")
                }
            else:
                processing_log[url] = {
                    "success": False,
                    "date_processed": datetime.now().isoformat(),
                    "error": "Failed to extract content"
                }
        
        self._save_processing_log(processing_log)
        return documents

class ContentGenerator:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.llm = OllamaLLM(
            model="llama3.2-vision",  # Using llama3.2-vision model
            base_url=base_url
        )
        self.prompt_template = PromptTemplate(
            input_variables=["question", "contexts"],
            template=GENERATION_PROMPT
        )
        
    def generate_response(self, question: str, contexts: List[Document]) -> str:
        # Format contexts into a string
        context_texts = []
        for i, doc in enumerate(contexts, 1):
            source = doc.metadata.get('source', 'Unknown source')
            title = doc.metadata.get('title', 'Unknown title')
            context_texts.append(f"[{i}] From {title} ({source}):\n{doc.page_content}\n")
        
        context_str = "\n".join(context_texts)
        
        # Generate prompt
        prompt = self.prompt_template.format(
            question=question,
            contexts=context_str
        )
        
        # Get response from LLM
        try:
            response = self.llm.invoke(prompt)
            return str(response)
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return f"Error generating response: {str(e)}"

def create_or_load_vectorstore(urls: List[str]):
    embed = OllamaEmbeddings(
        model="mxbai-embed-large",
        base_url="http://localhost:11434"
    )
    
    if os.path.exists(PERSIST_DIRECTORY) and os.path.isdir(PERSIST_DIRECTORY):
        print("Loading existing vector store...")
        try:
            vectorstore = Chroma(
                persist_directory=PERSIST_DIRECTORY,
                embedding_function=embed
            )
            
            processing_log = WebLoader(urls)._load_processing_log()
            new_urls = [url for url in urls if url not in processing_log or not processing_log[url]["success"]]
            
            if not new_urls:
                print("All URLs already processed. Using existing vector store.")
                return vectorstore, False
                
            print(f"Found {len(new_urls)} new URLs to process.")
            urls = new_urls
            
        except Exception as e:
            print(f"Error loading existing vector store: {str(e)}")
            return None, False
    else:
        print("Creating new vector store...")
        vectorstore = None
    
    loader = WebLoader(urls)

    print("Loading documents...")
    try:
        docs = loader.load()
        print(f"Number of documents loaded: {len(docs)}")
        
        if not docs:
            print("No new content to process")
            return vectorstore, False
            
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200, 
            add_start_index=True
        )

        print("Splitting documents...")
        all_splits = text_splitter.split_documents(docs)
        print(f"Number of splits created: {len(all_splits)}")
        
        if not all_splits:
            print("No splits created from documents")
            return None, False
            
        print("Creating/updating vector store...")
        texts = [doc.page_content for doc in all_splits]
        metadata = [doc.metadata for doc in all_splits]
        
        if vectorstore is None:
            vectorstore = Chroma.from_texts(
                texts=texts,
                embedding=embed,
                metadatas=metadata,
                persist_directory=PERSIST_DIRECTORY
            )
        else:
            vectorstore.add_texts(texts=texts, metadatas=metadata)
        
        print("Vector store updated successfully!")
        return vectorstore, True
            
    except Exception as e:
        print(f"Error processing documents: {str(e)}")
        import traceback
        print(f"Full traceback: {traceback.format_exc()}")
        return None, False

def query_and_generate(vectorstore, generator: ContentGenerator, query: str, k: int = 3):
    if not vectorstore:
        print("Vector store is not available for querying")
        return
        
    print(f"\n=== Processing Query: {query} ===\n")
    print("-" * 50)
    
    try:
        # Get results with relevance scores
        results = vectorstore.similarity_search_with_relevance_scores(
            query,
            k=k
        )
        
        if not results:
            print("No relevant results found")
            return
            
        # Extract documents from results
        documents = [doc for doc, score in results]
        
        # Generate response using the documents as context
        print("\nGenerating response...\n") # error
        response = generator.generate_response(query, documents)
        
        print("Generated Response:")
        print("-" * 30)
        print(response)
        print("-" * 30)
        
        print("\nSource Documents:")
        for doc, score in results:
            print(f"\nRelevance Score: {score:.4f}")
            print(f"Source: {doc.metadata.get('source', 'Unknown')}")
            print(f"Title: {doc.metadata.get('title', 'Unknown')}")
            print(f"Content:\n{doc.page_content}")
            print("-" * 30)
            
    except Exception as e:
        print(f"Error during query and generation: {str(e)}")

def main():
    # List of URLs to process
    urls = [
        "https://www.who.int/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines",
        "https://www.who.int/news-room/questions-and-answers/item/who-global-air-quality-guidelines",
        "https://www.cleanairfund.org/geography/india/",
        "https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war",
        "https://www.cs.ccu.edu.tw/~wildwolf/",
        "https://scholar.google.com/citations?user=y-3bZL4AAAAJ&hl=en"
    ]
    
    # Create content generator
    generator = ContentGenerator()
    
    # Create or load the vector store
    vectorstore, is_new = create_or_load_vectorstore(urls)
    
    if vectorstore:
        if is_new:
            print("Vector store updated with new content.")
        else:
            print("Using existing vector store.")
        
        # Example queries
        queries = [
            "who is Ching-Che Chung"
        ]
        
        for query in queries:
            query_and_generate(vectorstore, generator, query)
    else:
        print("Failed to create/load vector store. Cannot process queries.")

if __name__ == "__main__":
    main()