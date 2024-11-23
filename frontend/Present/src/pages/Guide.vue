<template>
  <div :class="$style.guide">
    <div :class="$style.bb" />
  
    <header :class="$style.topParent">
      <div :class="$style.top" />
      <img :class="$style.logo1Icon" alt="" src="/logo-1@2x.png" />
    </header>
    <main :class="$style.backgroundParent">
      <div :class="$style.background" />
     
      <div :class="$style.qOutputParent">
        <div :class="$style.qOutput" />
        <img
          :class="$style.frameChild"
          loading="lazy"
          alt="Arrow1"
          src="/arrow-12@2x.png"
        />
      </div>
      <div :class="$style.aOutputParent">
        <div :class="$style.aOutput" />
        <img
          :class="$style.frameItem"
          loading="lazy"
          alt="Arrow2"
          src="/arrow-13@2x.png"
        />
      </div>
      <!-- 替換成 next.png -->
      <img
        :class="$style.nextButton"
        loading="lazy"
        alt="Next"
        src="/next.png"
        @click="goToGuideShow"
      />
      <!-- 新增描述文字 -->
      <div :class="$style.instructions">
        <p>The words will show at right side.</p>
        <p>The answer given by the system will show at the left side.</p>
        <p>Press "Next" to move on.</p>
      </div>
    </main>
  </div>
</template>


<script lang="ts">
import { defineComponent } from "vue";
import FrameComponent1 from "../components/FrameShow1.vue";

export default defineComponent({
  name: "Guide",
  components: { FrameComponent1 },
  methods: {
    goToGuideShow() {
      this.$router.push({ name: "GuideShow" }); // 跳轉到名稱為 GuideShow 的路由
    },
  },
});
</script>




<style module>
  .top {
    position: absolute;
    top: 24px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: var(--color-cadetblue-200);
    width: 1840px;
    height: 161px;
    z-index: 2;
  }
  .logo1Icon { /*logo*/ 
    position: absolute;
    top: -9px;
    left: 800px;
    width: 240px;
    height: 207px;
    object-fit: cover;
    z-index: 3;
  }
  .topParent { /*top*/
    position: absolute;
    top: 0px;
    left: 40px;
    width: 1840px;
    height: 198px;
  }
  .qOutput { /* red1*/
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: var(--color-lightcoral);
    width: 567px;
    height: 196px;
    z-index: 2;
  }
  .frameChild {   /* arraow1*/
    position: absolute;
    top: 127.2px;
    left: 150.2px;
    width: 184.5px;
    height: 252.6px;
    overflow: hidden;
    object-fit: contain;
    z-index: 3;
  }
  .qOutputParent {
    position: absolute;
    top: 215px;
    left: 1165px;
    width: 567px;
    height: 379.8px;
  }
  .aOutput {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: var(--color-mistyrose);
    width: 567px;
    height: 196px;
    z-index: 3;
  }
  .frameItem {/*arraow2*/
    position: absolute;
    top: 96.4px;
    left: 501.7px;
    width: 332.5px;
    height: 185.4px;
    overflow: hidden;
    object-fit: contain;
    z-index: 4;
  }
  .aOutputParent {
    position: absolute;
    top: 427px;
    left: 136px;
    width: 834.2px;
    height: 281.8px;
  }
  .backgroundParent {
    position: absolute;
    top: 24px;
    left: 40px;
    box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.25);
    border-radius: var(--br-3xs);
    background-color: var(--color-gainsboro);
    width: 1840px;
    height: 1013px;
    max-width: 100%;
    z-index: 1;
  }
  
  .guide {
    width: 100%;
    height: 1080px;
    position: relative;
    background-color: var(--color-lavenderblush);
    overflow: hidden;
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
</style>
