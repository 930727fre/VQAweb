# rag-model/Dockerfile
FROM python:3.9

WORKDIR /app

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製程式碼
COPY . .

# 啟動 RAG 模型服務
CMD ["python", "main_B.py"]
