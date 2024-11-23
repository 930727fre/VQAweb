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

    // 發送按鈕的點擊事件
    const onSendClick = () => {
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
  
  /* 自定義上傳按鈕樣式 */
  .customUploadButton {
    width: 750px;
    border: none;
    outline: none;
    background-color: var(--color-cadetblue-100);
    border-radius: var(--br-3xs) 0px 0px var(--br-3xs);
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-7xl) var(--padding-11xl);
    box-sizing: border-box;
    font-family: var(--font-roboto);
    font-size: var(--font-size-5xl);
    color: var(--color-gray);
    max-width: 100%;
    z-index: 2;
  }

  /* 滑鼠移入時的背景顏色 */
  .customUploadButton:hover {
    background-color: var(--color-skyblue);
  }
  
  /* 輸入框容器 */
  .forInputPic {
    height: 7.5%;
    width: 39%;
    position: relative;
    max-width: 100%;
    z-index: 2;
  }
  .mid {
    height: 81px;
    width: 51px;
    position: relative;
    background-color: var(--color-steelblue);
    z-index: 2;
  }
  /* 輸入框背景顏色 */
  .contextinput {
    width: 100%;
    border: none;
    outline: none;
    background-color: var(--color-cadetblue-100);
    flex: 1;
    border-radius: 0px var(--br-3xs) var(--br-3xs) 0px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-7xl) var(--padding-9xl);
    box-sizing: border-box;
    font-family: var(--font-roboto);
    font-size: var(--font-size-5xl);
    color: var(--color-gray);
    min-width: 300px;
    max-width: 100%;
  }
  
  /* 滑鼠移入時的背景顏色 */
  .contextinput:hover {
    background-color: var(--color-skyblue);
  }
  
  /* 發送按鈕圖標樣式 */
  .sendIcon {
    width: 74px;
    height: 74px;
    position: relative;
    overflow: hidden;
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
    flex: 1;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: center;
    flex-wrap: wrap;
    align-content: flex-end;
    gap: var(--gap-0);
    row-gap: 20px;
    max-width: 100%;
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
  }
  /* 顯示檔案名稱的樣式 */
  .fileName {
    margin-top: 10px;
    font-size: var(--font-size-md);
    color: var(--color-gray);
  }

  /* 響應式設計，當螢幕寬度小於450px時，改變按鈕文字大小 */
  @media screen and (max-width: 450px) {
    .uploadThePicture {
      font-size: var(--font-size-lgi);
    }
  }
</style>
