# VQAweb
The multimodal answering system based on RAG.

## 執行方法 (Linux terminal)
★ 需用到 docker、docker-compose，若還沒安裝，可執行 ```./Ubuntu-install-docker.sh``` 安裝腳本
1. ```git clone -b integration https://github.com/930727fre/VQAweb.git```
2. ```cd VQAweb```
3. ```./docker_run.sh ```

   ※若無法執行，請先 ```chmod +x ./docker_run.sh``` 再執行
4. 至瀏覽器輸入 ```localhost:8000``` 即可

   ※ 若是在 server 上部署執行，請將 VQAweb/frontend/Present/src/components/Pictureinput.vue 裡 ```axios.post``` 那行的 ```localhost``` 改成 ```<server_IP>```
5. 取消執行： 至 terminal ```ctrl + C``` 即可

   ※若 docker 映像檔沒有成功刪除，請自行修改 ```./docker_run.sh``` 裡的 ```docker rmi``` 指令
