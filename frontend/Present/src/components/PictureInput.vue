<template>
  <div :class="$style.pictureInput">
    <div :class="$style.imageUpload">
      <div :class="$style.forInputPic">
        <!-- 隱藏檔案選擇框 -->
        <input
          ref="fileInputRef"
          :class="$style.uploadThePicture"
          type="file"
          accept="image/*"
          @change="onFileChange" 
        />
        <!-- 自定義的選擇按鈕，顯示檔案名稱 -->
        <div :class="$style.customUploadButton" @click="triggerFileInput">
          {{ fileName || 'Upload the picture' }} <!-- 點擊此按鈕觸發檔案選擇 -->
        </div>
      </div>
      <div :class="$style.mid" />
      <!-- 文本輸入框 -->
      <input
        v-model="question"
        :class="$style.contextinput "
        placeholder="Type your Question"  
        type="text"
      />
      <div :class="$style.submitButton">
        <!-- 發送按鈕 -->
        <img
          :class="$style.sendIcon"
          loading="lazy"
          alt="send icon"
          src="/send.svg"
          @click="onSendClick"  
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";
import axios from 'axios';

const frontend_port = 3000

export default defineComponent({
  name: "PictureInput",
  setup() {
    const fileInputRef = ref<HTMLInputElement | null>(null);
    const router = useRouter();
    const question = ref(""); // 用戶輸入的問題
    const selectedImage = ref<string | null>(null); // 存儲上傳的圖片數據
    const fileName = ref<string | null>(null); // 存儲圖片檔名


    // 處理檔案變更事件
    const onFileChange = (event: Event) => {
      const input = event.target as HTMLInputElement;
      const file = input.files ? input.files[0] : null;

      if (file) {
        fileName.value = file.name;
        // 使用 FileReader 將圖片轉為 Base64 格式
        const reader = new FileReader();
        reader.onload = (e) => {
          selectedImage.value = e.target?.result as string;
          console.log("圖片已上傳：", selectedImage.value);
        };
        reader.readAsDataURL(file);
      } else {
        console.log("未選擇圖片文件");
      }
    };

    const sendDataToBackend = async (imageFile: File, inputText: string) => {
      const formData = new FormData();
      formData.append("image", imageFile); // input圖片
      formData.append("text", inputText); // input文字

      try {
        const response = await axios.post(`http://localhost:${frontend_port}/upload`, formData, {
          headers: {
            "Content-Type": "multipart/form-data", // 告訴後端這是表單數據
          },
        });
        console.log("後端回應：", response.data.reponse); // 處理後端回應
      } catch (error) {
        console.error("發送資料到後端時出現錯誤：", error);
      }
    };

    // 發送按鈕的點擊事件
    const onSendClick = () => {
      if (!question.value || !fileInputRef.value?.files?.[0]) {
        console.log("請選擇圖片並輸入問題");
        return;
      }
      const imageFile = fileInputRef.value.files[0]; // 取得選擇的圖片檔案
      sendDataToBackend(imageFile, question.value); // 發送資料到後端
      router.push({
        path: '/result',
        query: {
          question: question.value, // 傳送問題
          image: selectedImage.value || '' // 傳送圖片（若有選擇）
        }
      });
    };

    // 觸發檔案輸入框的點擊事件
    const triggerFileInput = () => {
      fileInputRef.value?.click(); // 使用 ref 來觸發檔案輸入框的點擊
    };

    return {
      question,
      selectedImage,
      onFileChange,
      onSendClick,
      triggerFileInput,
      fileInputRef,  
      fileName,
    };
  },
});
</script>

<style module>
  /* 整體圖片輸入區域 */
  .picInput {
    position: absolute;
    bottom: 0px;
    left: 0px;
    border-radius: var(--br-3xs) 0px 0px var(--br-3xs);
    background-color: var(--color-cadetblue-100);
    width: 100%;
    height: 100%;
    cursor: pointer;
  }
  
  /* 隱藏原始檔案選擇框 */
  .uploadThePicture {
    display: none;
  }
  
  
  /* 滑鼠移入時的背景顏色 */
  .customUploadButton:hover {
    background-color: var(--color-skyblue);
  }
  
  /* 輸入框容器 */
  .forInputPic {
    height: 7.5%;
    width: 39%;
    position: fixed; /* 設定絕對定位 */
    left: 10%;
    max-width: 100%;
    z-index: 2;
  }
  .mid {
    position: fixed; /* 設定絕對定位 */
    left: 48%;
    height: 7.5vh;
    width: 4%;
    background-color: var(--color-steelblue);
    z-index: 2;
  }
  /* 自定義上傳按鈕樣式 */
  .customUploadButton {
    position: fixed; /* 設定絕對定位 */
    left: 10%;
    width: 38%;
    height: 7.5vh;
    overflow: hidden; /* 隱藏溢出的內容 */
    border: none;
    outline: none;
    background-color: var(--color-cadetblue-100);
    border-radius: var(--br-3xs) 0px 0px var(--br-3xs);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: var(--padding-7xl) var(--padding-9xl);
    box-sizing: border-box;
    font-family: var(--font-roboto);
    font-size: 2.5vh;
    color: var(--color-gray);
    max-width: 100%;
  }
  /* 輸入框背景顏色 */
  .contextinput {
    position: fixed; /* 設定絕對定位 */
    width: 36%;
    left: 52%;
    height: 7.5%;
    border: none;
    outline: none;
    background-color: var(--color-cadetblue-100);
    border-radius: 0px var(--br-3xs) var(--br-3xs) 0px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: var(--padding-7xl) var(--padding-9xl);
    box-sizing: border-box;
    font-family: var(--font-roboto);
    font-size: 2.5vh;
    color: var(--color-gray);
    max-width: 40%;
  }
  
  /* 滑鼠移入時的背景顏色 */
  .contextinput:hover {
    background-color: var(--color-skyblue);
  }
  
  /* 發送按鈕圖標樣式 */
  .sendIcon {
    width: 8%;
    height: 8%;
    position: absolute;
    overflow: hidden;
    right: 3%;
    bottom: 0.01%;
    flex-shrink: 0;
    cursor: pointer;
    z-index: 4;
  }
  
  /* 按鈕容器 */
  .submitButton {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px 0px var(--padding-10xs);
  }
  
  /* 圖片上傳區域容器 */
  .imageUpload {
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: center;
    flex-wrap: wrap;
    align-content: flex-end;
    gap: var(--gap-0);
    row-gap: 1%;
    max-width: 100%;
    height: 100%; /* 確保它有高度 */
  }
  
  /* 整體圖片輸入區域容器 */
  .pictureInput {
    width: 90.5%;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px var(--padding-24xl);
    box-sizing: border-box;
    max-width: 100%;
    height: 100%;
  }
  /* 顯示檔案名稱的樣式 */
  .fileName {
    margin-top: 10px;
    font-size: var(--font-size-md);
    color: var(--color-gray);
  }

</style>
