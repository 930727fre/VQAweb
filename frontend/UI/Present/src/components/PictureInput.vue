<template>
  <div :class="$style.pictureInput">
    <div :class="$style.imageUpload">
      <div :class="$style.forInputPic">
        <div :class="$style.picInput" @click="onPicInputClick"></div>
        
        <!-- 更改這裡為 type="file" 並監聽 change 事件 -->
        <input
          :class="$style.uploadThePicture"
          placeholder="Upload the picture"
          type="file"
          accept="image/*"
          @change="onFileChange"
        />
      </div>
      <div :class="$style.mid"></div>
      <input
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
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "PictureInput",
    methods: {
      onFileChange(event: Event) {
        const input = event.target as HTMLInputElement;
        const file = input.files ? input.files[0] : null;
        if (file) {
          // 這裡可以處理圖片文件，例如上傳圖片或進行其他處理
          console.log("已選擇圖片文件：", file);
        } else {
          console.log("未選擇圖片文件");
        }
    },
      onPicInputClick() {
        this.$router.push("/");
      },
      onSendClick() {
        this.$router.push("/result");
      },
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
