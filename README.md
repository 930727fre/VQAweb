# VQAweb

A multimodal answering system based on RAG.

## System Specifications

- **Machine Type**: `n1-standard-8`
    - vCPUs: 8
    - RAM: 30 GiB
- **GPU**: NVIDIA T4 (1 unit)
- **Operating System**: Ubuntu 22.04 LTS

## Dependencies

- **Git LFS**
- **Docker**
- **Docker Compose**
- **CUDA Driver**
- **cuDNN**

For a hassle-free installation, run the `GCP-install-dependencies.sh` script to install all required dependencies on a Ubuntu GCP instance.

## How to Set Up Models

This project requires `.h5` model files to run properly. Follow these steps to set up the models:

1. **Ensure `git` and `git-lfs` are installed**
    
    If you don’t have Git LFS installed, you can install it by running:
    
    ```bash
    git lfs install
    ```
    
2. **Navigate to the `backend` directory**
    
    Change into the `VQAweb/backend` directory where the models will be set up:
    
    ```bash
    cd VQAweb/backend
    ```
    
3. **Clone the `VQAmodels` repository**
    
    Clone the `VQAmodels` repository from Hugging Face:
    
    ```bash
    git clone https://huggingface.co/930727fre/VQAmodels models
    ```
    
4. **Move the `.h5` files to the parent directory**
    
    Move the `.h5` model files from the `models` directory to the `VQAweb/backend` directory:
    
    ```bash
    mv models/*.h5 .
    ```
    
5. **Remove the empty `models` directory**
    
    Once the files are moved, remove the now-empty `models` directory:
    
    ```bash
    sudo rm -drf models
    ```
    

## How to Run the Full Backend

1. The stable version is located in the `main` branch.
2. Navigate to the project directory:
    
    ```bash
    cd VQAweb
    
    ```
    
3. Modify the file `VQAweb/frontend/Present/src/components/Pictureinput.vue`:
    
    Replace `localhost` in the `axios.post` line with your `<server_IP>`.
    
4. Run the backend using the following script:
    
    ```bash
    ./docker_run.sh
    
    ```
    
    If you encounter execution issues, make the script executable first:
    
    ```bash
    chmod +x ./docker_run.sh
    ./docker_run.sh
    
    ```
    
5. Access the application in your browser:
    
    Visit `<server_IP>:8000` in your web browser.
    
6. To stop the application:
    
    Press `Ctrl + C` in the terminal.
    
    **Note:**
    
    If Docker images are not successfully deleted, manually modify the `docker rmi` command in the `./docker_run.sh` script to remove them.
