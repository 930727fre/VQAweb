#!/bin/bash
sudo rm -drf vectorstore_db
# Step 1: Build the Docker image
docker build -t backend .

# Step 2: Run the Docker container
docker run --rm -v $(pwd):/app -w /app --network host --gpus all --name backend backend
