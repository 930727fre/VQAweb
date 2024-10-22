# multimodel-model/Dockerfile
FROM tensorflow/tensorflow:latest-gpu

WORKDIR /app

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製程式碼
COPY . .

# 啟動模型處理服務
CMD ["python", "main_A.py"]
