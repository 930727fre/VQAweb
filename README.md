# VQAweb
The multimodal answering system based on RAG.

## The imagined file structure tree
```CSS
/project-root
│
├── api/
│   └── Dockerfile
│   └── main.py
│   └── requirements.txt
├── frontend/
│   └── Dockerfile
│   └── src/
│   └── package.json
│   └── package-lock.json
├── multimodel-model/  # 後端組A (CNN, RNN)
│   └── Dockerfile
│   └── main_A.py
│   └── requirements.txt
├── rag-model/  # 後端組B (RAG, LLM)
│   └── Dockerfile
│   └── main_B.py
│   └── requirements.txt
└── docker-compose.yml
```
