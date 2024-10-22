# frontend/Dockerfile
FROM node:14

WORKDIR /app

# 複製 package.json 和 package-lock.json 並安裝依賴
COPY package*.json ./
RUN npm install

# 複製其餘前端程式碼
COPY . .

# 啟動前端應用
CMD ["npm", "run", "serve"]
