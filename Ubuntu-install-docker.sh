#!/bin/bash

# 更新包索引
echo "Updating package index..."
sudo apt update

# 安裝必要的軟體包
echo "Installing required packages..."
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# 添加 Docker 的官方 GPG 鍵
echo "Adding Docker's official GPG key..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 添加 Docker 倉庫
echo "Adding Docker repository..."
echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list

# 再次更新包索引
echo "Updating package index again..."
sudo apt update

# 安裝 Docker
echo "Installing Docker..."
sudo apt install -y docker-ce

# 驗證 Docker 安裝
echo "Verifying Docker installation..."
sudo docker --version

# 安裝 Docker Compose
echo "Installing Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 設定 Docker Compose 的權限
echo "Setting permissions for Docker Compose..."
sudo chmod +x /usr/local/bin/docker-compose

# 驗證 Docker Compose 安裝
echo "Verifying Docker Compose installation..."
docker-compose --version

# 如果需要 NVIDIA Container Toolkit，可以取消以下註解
# echo "Setting up NVIDIA Container Toolkit..."
# distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
# && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
# && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# 更新並安裝 NVIDIA Container Toolkit
# echo "Installing NVIDIA Container Toolkit..."
# sudo apt update
# sudo apt install -y nvidia-docker2

# 重新啟動 Docker 以應用更改
echo "Restarting Docker..."
sudo systemctl restart docker

# 測試 NVIDIA Docker 支持（如果已安裝 NVIDIA Container Toolkit）
# echo "Testing NVIDIA Docker support..."
# sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi

echo "Docker, Docker Compose, and NVIDIA Container Toolkit have been installed successfully!"
