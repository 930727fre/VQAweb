sudo apt update
sudo apt upgrade
sudo apt install rsync
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
getent group docker
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

echo "Installing Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 設定 Docker Compose 的權限
echo "Setting permissions for Docker Compose..."
sudo chmod +x /usr/local/bin/docker-compose

# 驗證 Docker Compose 安裝
echo "Verifying Docker Compose installation..."
docker-compose --version



sudo apt install neofetch
sudo apt remove --purge gcc g++
sudo apt autoremove
# Add the PPA if needed (optional for older versions)
sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y
sudo apt update
# Install GCC-12
sudo apt install gcc-12 g++-12
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 20
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 20
sudo ln -sf /usr/bin/gcc-12 /usr/bin/cc

sudo systemctl stop google-cloud-ops-agent
curl -L https://github.com/GoogleCloudPlatform/compute-gpu-installation/releases/download/cuda-installer-v1.1.0/cuda_installer.pyz --output cuda_installer.pyz
sudo python3 cuda_installer.pyz install_driver

#!/bin/bash
# Set the Miniconda installer URL
MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
INSTALLER="Miniconda3-latest-Linux-x86_64.sh"
# Download the Miniconda installer
echo "Downloading Miniconda..."
wget $MINICONDA_URL -O $INSTALLER
# Run the installer
echo "Running the Miniconda installer..."
bash $INSTALLER
# Check if the installation was successful
if [[ $? -ne 0 ]]; then
    echo "Miniconda installation failed."
    exit 1
fi
# Initialize Miniconda
echo "Initializing Miniconda..."
conda init
# Inform the user to restart the terminal
echo "Miniconda installation is complete."
echo "Please close and reopen your terminal for changes to take effect."
# Optionally, you can provide instructions to update conda
echo "To update conda, run: conda update conda"
echo "To create a new environment, use: conda create --name myenv python=3.8"

distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
       && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
       && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
             sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
             sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo systemctl restart docker
sudo docker run --rm --gpus all nvidia/cuda:12.5.1-devel-ubuntu22.04 nvidia-smi # test
