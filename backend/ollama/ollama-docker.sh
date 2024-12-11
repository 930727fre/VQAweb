docker pull ollama/ollama
docker run --gpus all --rm -d \
  -v ollama:/root/.ollama \
  -v "$(pwd):/data" \
  -p 11434:11434 \
  --name ollama ollama/ollama
docker exec -it ollama ollama run llama3.2-vision
# docker exec -it ollama ollama run llama3.2:3b
docker exec -it ollama ollama run mxbai-embed-large