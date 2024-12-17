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
    <div v-if="isProcessing" :class="$style.processingModal">
      <div :class="$style.modalContent">
        <p>Input successful! Please wait a few seconds</p>
      </div>
    </div>
    <div v-if="isuploadpicture" :class="$style.uploadModal">
      <div :class="$style.modalContent">
        <p>Please input question!</p>
      </div>
    </div>
    <div v-if="isinputquestion" :class="$style.inputquestionModal">
      <div :class="$style.modalContent">
        <p>Please input question and upload picture!</p>
      </div>
    </div>
  </div>
  </template>
 
 
 <script lang="ts">
 import { defineComponent, ref } from "vue";
 import { useRouter } from "vue-router";
 import axios from 'axios';
 
 
 export default defineComponent({
  name: "PictureInput",
  setup() {
    const isProcessing = ref(false);
    const isuploadpicture = ref(false);
    const isinputquestion = ref(false);
    const fileInputRef = ref<HTMLInputElement | null>(null);
    const router = useRouter();
    const question = ref(""); // 用戶輸入的問題
    const selectedImage = ref<string | null>(null); // 存儲上傳的圖片數據
    const fileName = ref<string | null>(null); // 存儲圖片檔名
    const response = ref("");
 
 
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
 
 
    const sendDataToBackend = async (imageFile?: File, inputText?: string) => {
    const formData = new FormData();
 
 
    // Only append if values are present
    if (imageFile) {
      formData.append("image", imageFile);
    }
    if (inputText) {
      formData.append("text", inputText);
    }
 
 
    try {
      const response = await axios.post(`http://localhost:8000/api/upload`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      console.log("後端回應：", response.data.response);
      router.push({
        path: '/result',
        query: {
          question: inputText || '',
          image: selectedImage.value || '',
          answer: response.data.response || 'No Response.'
        },
      });
    } catch (error) {
      console.error("發送資料到後端時出現錯誤：", error);
    }
  };
 
 
  // 發送按鈕的點擊事件
  const onSendClick = () => {
    const imageFile = fileInputRef.value?.files?.[0];
    const inputText = question.value;
    // Optional: Add a check to ensure at least one input is provided
    if(!inputText && imageFile){
      isuploadpicture.value = true;
      isinputquestion.value = false;
      console.log("請至少選擇圖片或輸入文字");
      return;
    }
    else if (!inputText && !imageFile) {
      isuploadpicture.value = false;
      isinputquestion.value = true;
      console.log("請至少選擇圖片或輸入文字");
      return;
    }
    else{
      isProcessing.value = true; // 顯示「系統正在運算中」提示框
      isuploadpicture.value = false;
      isinputquestion.value = false;
      sendDataToBackend(imageFile, inputText); 
    }
  };
 
 
 
 
    // 觸發檔案輸入框的點擊事件
    const triggerFileInput = () => {
      isuploadpicture.value = false;
      isinputquestion.value = false;
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
      isProcessing,
      isuploadpicture,
      isinputquestion,
    };
  },
 });
 </script>
 
 
 <style module>
  .processingModal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(165, 165, 165, 0.5); /* 半透明背景 */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 6; /* 保證層級最高 */
  }
  .modalContent {
  background-color: rgb(0, 5, 1);
  padding: 5px 10px;
  border-radius: var(--br-3xs);
  text-align: center;
  font-family: var(--font-roboto);
  font-size: 18px;
  color: rgb(238, 243, 239);
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
  z-index: 7;
 }
 .uploadModal{
    position: fixed;
    top: 40%;
    left: 0%;
    width: 100%;
    height: 50%;
    background-color: rgba(0, 0, 0, 0); /* 半透明背景 */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10; /* 保證層級最高 */
  }
 .inputquestionModal {
    position: fixed;
    top: 40%;
    left: 0%;
    width: 100%;
    height: 50%;
    background-color: rgba(0, 0, 0, 0); /* 半透明背景 */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 5;
  }
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
 
 
 
 
 
 
