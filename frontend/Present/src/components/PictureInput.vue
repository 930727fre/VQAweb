<template>
  <div :class="$style.pictureInput">
    <div :class="$style.imageUpload">
      <div :class="$style.forInputPic">
        <div :class="$style.picInput" @click="onSendClick"></div>
        
        <!-- 文件輸入框 -->
        <input
          :class="$style.uploadThePicture"
          type="file"
          accept="image/*"
          @change="onFileChange"
        />
      </div>
      <!-- 文本輸入框 -->
      <input
        v-model="question"
        :class="$style.imageUploadChild"
        placeholder="Type your Question"
        type="text"
      />
      <div :class="$style.submitButton">
        <img
          :class="$style.sendIcon"
          loading="lazy"
          alt=""
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
    const router = useRouter();
    const question = ref(""); // 文本輸入的數據
    const selectedImage = ref<string | null>(null); // 存儲上傳的圖片文件

    const onFileChange = (event: Event) => {
      const input = event.target as HTMLInputElement;
      const file = input.files ? input.files[0] : null;

      if (file) {
        // 將圖片文件轉為 Base64 URL
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

    const onSendClick = () => {
      router.push({
        path: '/result',
        query: {
          question: question.value,
          image: selectedImage.value || ''
        }
      });
    };


    return {
      question,
      selectedImage,
      onFileChange,
      onSendClick,
    };
  },
});
</script>
<style module>
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
  .uploadThePicture {
    width: 100%;
    border: none;
    outline: none;
    font-family: var(--font-roboto);
    font-size: var(--font-size-5xl);
    background-color: transparent;
    position: absolute;
    bottom: 26px;
    left: 30px;
    color: var(--color-gray);
    text-align: left;
    display: flex;
    align-items: center;
    height: 29px;
    padding: 0;
    z-index: 1;
  }
  .forInputPic {
    height: 81px;
    width: 750px;
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
  .imageUploadChild {
    width: 100%;
    border: none;
    outline: none;
    background-color: var(--color-skyblue);
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
  .sendIcon {
    width: 74px;
    height: 74px;
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
    cursor: pointer;
    z-index: 4;
  }
  .submitButton {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px 0px var(--padding-10xs);
  }
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
  .pictureInput {
    width: 1738px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px var(--padding-24xl);
    box-sizing: border-box;
    max-width: 100%;
  }

  @media screen and (max-width: 450px) {
    .uploadThePicture {
      font-size: var(--font-size-lgi);
    }
  }
</style>
