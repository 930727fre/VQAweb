<template>
  <div :class="$style.tapQuest" @click.stop>
    <main :class="$style.layout" @click.stop>
      <div :class="$style.bb" />
      <img :class="$style.logo1Icon" alt="" src="/logo-1@2x.png" />
      <section :class="$style.contentArea" @click.stop>
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
      <img
        :class="$style.arrowright"
        loading="lazy"
        alt=""
        src="/arrow-121@2x.png"
        @click.stop
      />
      <img
        :class="$style.arrowright2"
        loading="lazy"
        alt=""
        src="/arrow-131@2x.png"
        @click.stop
      />
      <img
        :class="$style.nextButton"
        loading="lazy"
        alt="Next"
        src="/next.png"
        @click="handleNextClick"
      />
      <div :class="$style.instructions">
        <p>You can input your picture at left side.</p>
        <p>Type in your question at right side.</p>
        <p>Press "Next" to move on.</p>
      </div>
    </main>
  </div>
</template>


<script lang="ts">
import { defineComponent, onMounted, onUnmounted } from "vue";
import PictureInput from "../components/PictureInput.vue";

export default defineComponent({
  name: "TapQuest",
  components: { PictureInput },
  methods: {
    handleNextClick() {
      this.$router.push({ name: "Guide" });
    },
    preventOtherClicks(e: MouseEvent) {
      const target = e.target as HTMLElement;
      if (!target.closest(`.${this.$style.nextButton}`)) {
        e.stopImmediatePropagation();
        e.preventDefault();
      }
    },
  },
  mounted() {
    document.addEventListener("click", this.preventOtherClicks, true); // 捕获阶段阻止事件
  },
  unmounted() {
    document.removeEventListener("click", this.preventOtherClicks, true); // 移除监听器
  },
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
  .nextButton {
    position: absolute;
    top: 550px; /* 可根據需求調整位置 */
    left: 1450px; /* 可根據需求調整位置 */
    width: 200px; /* 控制圖片大小 */
    height: 252px; /* 控制圖片大小 */
    object-fit: contain; /* 確保圖片按比例縮放 */
    z-index: 3;
  }
  .instructions {
    position: absolute;
    top: 600px; /* 調整文字說明的位置 */
    left: 1000px; /* 調整文字說明的位置 */
    width: 300px; /* 控制文字容器寬度 */
    text-align: center; /* 居中對齊 */
    font-size: 18px; /* 設定文字大小 */
    color: #333; /* 設定文字顏色 */
    font-family: Arial, sans-serif; /* 字體設定 */
    z-index: 4;
    background: rgba(255, 255, 255, 0.8); /* 半透明背景提高可讀性 */
    padding: 10px 20px; /* 增加內邊距 */
    border-radius: 8px; /* 圓角效果 */
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); /* 添加陰影 */
  }
  .arrowright{
    position: absolute;
    top: 706.4px;
    left: 1273.5px;
    width: 166.9px;
    height: 222.1px;
    overflow: hidden;
    object-fit: contain;
    z-index: 3;
  }
  .arrowright2{
    position: absolute;
    top: 606.4px;
    left: 733.5px;
    width: 300.9px;
    height: 360.1px;
    overflow: hidden;
    object-fit: contain;
    z-index: 3;
  }
  @media screen and (max-width: 1408px) {
    .layout {
      height: auto;
      min-height: 1080px;
    }
  }
</style>
