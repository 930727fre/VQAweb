#!/bin/bash

# Update the package index
echo "Updating package index..."
sudo apt update

# Install required packages
echo "Installing required packages..."
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's official GPG key
echo "Adding Docker's official GPG key..."
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

# Add the Docker repository
echo "Adding Docker repository..."
echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list

# Update the package index again
echo "Updating package index again..."
sudo apt update

# Install Docker
echo "Installing Docker..."
sudo apt install -y docker-ce

# Verify Docker installation
echo "Verifying Docker installation..."
sudo docker --version

# Install Docker Compose
echo "Installing Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Set permissions for Docker Compose
echo "Setting permissions for Docker Compose..."
sudo chmod +x /usr/local/bin/docker-compose

# Verify Docker Compose installation
echo "Verifying Docker Compose installation..."
docker-compose --version

# Set up the NVIDIA Container Toolkit
echo "Setting up NVIDIA Container Toolkit..."
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
&& curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
&& curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# Update and install NVIDIA Container Toolkit
echo "Installing NVIDIA Container Toolkit..."
sudo apt update
sudo apt install -y nvidia-docker2

# Restart Docker to apply changes
echo "Restarting Docker..."
sudo systemctl restart docker

# Test NVIDIA Docker support
echo "Testing NVIDIA Docker support..."
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi

echo "Docker, Docker Compose, and NVIDIA Container Toolkit have been installed successfully!"
