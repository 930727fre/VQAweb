curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2-vision",
  "prompt": "hi"
}'
curl http://localhost:11434/api/embed -d '{
  "model": "mxbai-embed-large",
  "input": "Why is the sky blue?"
}'