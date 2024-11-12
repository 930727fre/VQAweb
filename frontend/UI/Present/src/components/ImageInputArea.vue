<template>
  <div :class="$style.imageInputArea">
    <div :class="$style.imageUpload">
      <div :class="$style.forInputPic">
        <div :class="$style.picInput" @click="onPicInputClick" />
        <input
          :class="$style.uploadThePicture"
          placeholder="Upload the picture"
          type="text"
        />
      </div>
      <div :class="$style.mid" />
      <FrameComponent />
      <div :class="$style.submissionArea">
        <img
          :class="$style.sendIcon"
          loading="lazy"
          alt=""
          src="/send1.svg"
          @click="onSendClick"
        />
      </div>
    </div>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";
  import FrameComponent from "./FrameComponent.vue";

  export default defineComponent({
    name: "ImageInputArea",
    components: { FrameComponent },
    methods: {
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
    height: 100%;
    width: 100%;
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    border-radius: var(--br-3xs) 0px 0px var(--br-3xs);
    background-color: var(--color-cadetblue-100);
    cursor: pointer;
  }
  .uploadThePicture {
    width: calc(100% - 518px);
    border: none;
    outline: none;
    font-family: var(--font-roboto);
    font-size: var(--font-size-5xl);
    background-color: transparent;
    position: absolute;
    height: calc(100% - 52px);
    top: 26px;
    left: 30px;
    color: var(--color-gray);
    text-align: left;
    display: flex;
    align-items: center;
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
  .sendIcon {
    width: 74px;
    height: 74px;
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
    cursor: pointer;
    z-index: 4;
  }
  .submissionArea {
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
    justify-content: flex-start;
    flex-wrap: wrap;
    align-content: flex-end;
    gap: var(--gap-0);
    row-gap: 20px;
    max-width: 100%;
  }
  .imageInputArea {
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
