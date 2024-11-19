<template>
  <div :class="$style.tapQuest">
    <main :class="$style.layout">
      <div :class="$style.bb" />
      <img :class="$style.logo1Icon" alt="" src="/logo-1@2x.png" />
      <section :class="$style.contentArea">
        <div :class="$style.background" />
        <div :class="$style.questionInput">
          <header :class="$style.top" />
          <div :class="$style.outputAreaWrapper">
            <div :class="$style.outputArea">
              <div :class="$style.qandA">
                <section :class="$style.qOutput" rows="10" cols="28" />
              </div>
              <section :class="$style.aOutput" rows="10" cols="28" />
            </div>
          </div>
        </div>
        <PictureInput />
      </section>
    </main>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";
  import PictureInput from "../components/PictureInput.vue";

  export default defineComponent({
    name: "TapQuest",
    components: { PictureInput },
  });
</script>
<style module>
  .bb {
    position: absolute;
    top: 0px;
    left: 0px;
    background-color: var(--color-lavenderblush);
    width: 100%;
    height: 100%;
    display: none;
  }
  .logo1Icon {
    position: absolute;
    height: calc(100% - 873px);
    width: calc(100% - 1680px);
    top: -9px;
    right: 840px;
    bottom: 882px;
    left: 840px;
    max-width: 100%;
    overflow: hidden;
    max-height: 100%;
    object-fit: cover;
    z-index: 3;
  }
  .background {
    align-self: stretch;
    height: 1013px;
    position: relative;
    box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.25);
    border-radius: var(--br-3xs);
    background-color: var(--color-gainsboro);
    display: none;
  }
  .top {
    align-self: stretch;
    height: 161px;
    position: relative;
    border-radius: var(--br-3xs);
    background-color: var(--color-cadetblue-200);
    z-index: 2;
  }
  .qOutput {
    border: none;
    background-color: var(--color-lightcoral);
    height: 196px;
    width: 567px;
    outline: none;
    position: relative;
    border-radius: var(--br-3xs);
    max-width: 100%;
    z-index: 2;
  }
  .qandA {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-end;
    max-width: 100%;
  }
  .aOutput {
    border: none;
    background-color: var(--color-mistyrose);
    height: 196px;
    width: 567px;
    outline: none;
    position: relative;
    border-radius: var(--br-3xs);
    max-width: 100%;
    z-index: 2;
  }
  .outputArea {
    width: 1596px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-base);
    max-width: 100%;
  }
  .outputAreaWrapper {
    width: 1812px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
    padding: 0px var(--padding-xl);
    box-sizing: border-box;
    max-width: 100%;
  }
  .questionInput {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: flex-start;
    gap: var(--gap-35xl);
    max-width: 100%;
  }
  .contentArea {
    position: absolute;
    top: 24px;
    left: 40px;
    box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.25);
    border-radius: var(--br-3xs);
    background-color: var(--color-gainsboro);
    width: 1840px;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: flex-start;
    padding: 0px 0px var(--padding-25xl);
    box-sizing: border-box;
    gap: var(--gap-246xl);
    max-width: 100%;
    z-index: 1;
  }
  .layout {
    height: 1080px;
    flex: 1;
    position: relative;
    background-color: var(--color-lavenderblush);
    overflow: hidden;
    max-width: 100%;
  }
  .tapQuest {
    width: 100%;
    position: relative;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    line-height: normal;
    letter-spacing: normal;
  }

  @media screen and (max-width: 1408px) {
    .layout {
      height: auto;
      min-height: 1080;
    }
  }
</style>
