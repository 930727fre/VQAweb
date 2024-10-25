# api/Dockerfile
FROM python:3.9

WORKDIR /app

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt .

# Upgrade pip before installing requirements
RUN python3 -m pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有程式碼到容器中
COPY . .

# 啟動 FastAPI 應用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
