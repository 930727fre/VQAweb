<template>
  <div :class="$style.searchInputInner">
    <div :class="$style.forInputPicParent">
      <input
        :class="$style.forInputPic"
        placeholder="Upload the picture"
        type="text"
      />
      <div :class="$style.mid" />
      <FrameComponent />
      <div :class="$style.sendWrapper">
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
  import FrameComponent from "./FrameComponent.vue";

  export default defineComponent({
    name: "FrameComponent1",
    components: { FrameComponent },
    methods: {
      onSendClick() {
        this.$router.push("/result");
      },
    },
  });
</script>
<style module>
  .forInputPic {
    width: 750px;
    border: none;
    outline: none;
    background-color: var(--color-skyblue);
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
  .sendWrapper {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px 0px var(--padding-10xs);
  }
  .forInputPicParent {
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
  .searchInputInner {
    width: 1738px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px var(--padding-24xl);
    box-sizing: border-box;
    max-width: 100%;
    text-align: left;
    font-size: var(--font-size-5xl);
    color: var(--color-gray);
    font-family: var(--font-roboto);
  }
</style>
