To perform a demo without API (simply testing if RAG works fine)
1. Run `VQAweb/backend/ollama-docker.sh` to start all models
2. Modify `VQAweb/backend/Dockerfile` the line `CMD ["python3", "main.py"]` to `CMD ["python3", "demo.py"]`
3. Run `VQAweb/backend/backend.sh`

To perform a formal test (fastAPI + RAG)
1. Run `VQAweb/backend/ollama-docker.sh` to start all models
2. Run `VQAweb/backend/backend.sh`

Note: `sky.h5` and `air_v100.h5` should be stored at `VQAweb/backend`