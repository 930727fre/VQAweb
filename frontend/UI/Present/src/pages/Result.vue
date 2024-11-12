<template>
  <div :class="$style.result">
    <main :class="$style.layout">
      <div :class="$style.bb" />
      <section :class="$style.frameParent">
        <div :class="$style.backgroundParent">
          <div :class="$style.background" />
          <header :class="$style.top" />
          <textarea :class="$style.aOutput" rows="10" cols="28" />
          <div :class="$style.qOutputParent">
            <textarea :class="$style.qOutput" rows="10" cols="28" />
            <img
              :class="$style.sendIcon"
              loading="lazy"
              alt=""
              src="/send.svg"
            />
          </div>
        </div>
        <img :class="$style.logo1Icon" alt="" src="/logo-1@2x.png" />
      </section>
    </main>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "Result",
  });
</script>
<style module>
  .bb {
    height: 1080px;
    width: 1920px;
    position: relative;
    background-color: var(--color-lavenderblush);
    display: none;
    max-width: 100%;
  }
  .background {
    position: absolute;
    top: 0px;
    left: 0px;
    box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.25);
    border-radius: var(--br-3xs);
    background-color: var(--color-gainsboro);
    width: 100%;
    height: 100%;
    display: none;
  }
  .top {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: var(--color-cadetblue-200);
    width: 1840px;
    height: 161px;
    z-index: 2;
  }
  .aOutput {
    border: none;
    background-color: var(--color-mistyrose);
    height: 196px;
    width: 567px;
    outline: none;
    position: absolute;
    top: 427px;
    left: 136px;
    border-radius: var(--br-3xs);
    z-index: 2;
  }
  .qOutput {
    border: none;
    background-color: var(--color-lightcoral);
    height: 196px;
    width: 567px;
    outline: none;
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    z-index: 2;
  }
  .sendIcon {
    position: absolute;
    top: 677px;
    left: 558px;
    width: 74px;
    height: 74px;
    overflow: hidden;
    z-index: 4;
  }
  .qOutputParent {
    position: absolute;
    top: 215px;
    left: 1165px;
    width: 632px;
    height: 751px;
  }
  .backgroundParent {
    position: absolute;
    top: 24px;
    left: 0px;
    box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.25);
    border-radius: var(--br-3xs);
    background-color: var(--color-gainsboro);
    width: 1840px;
    height: 1013px;
    z-index: 1;
  }
  .logo1Icon {
    position: absolute;
    top: -9px;
    left: 800px;
    width: 240px;
    height: 207px;
    object-fit: cover;
    z-index: 3;
  }
  .frameParent {
    height: 1037px;
    flex: 1;
    position: relative;
    max-width: 100%;
  }
  .layout {
    flex: 1;
    background-color: var(--color-lavenderblush);
    overflow: hidden;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 40px var(--padding-24xl);
    box-sizing: border-box;
    max-width: 100%;
  }
  .result {
    width: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    line-height: normal;
    letter-spacing: normal;
  }

  @media screen and (max-width: 864px) {
    .layout {
      padding-bottom: var(--padding-9xl);
      box-sizing: border-box;
    }
  }
  @media screen and (max-width: 432px) {
    .layout {
      padding-bottom: var(--padding-xl);
      box-sizing: border-box;
    }
  }
</style>
