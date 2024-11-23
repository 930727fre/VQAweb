<template>
  <div :class="$style.tapQuest">
    <img :class="$style.logo1Icon" alt="" src="/logo-1@2x.png" />
    <main :class="$style.layout">
      <div :class="$style.bb" />
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
        <PictureInput :class="$style.fixedPictureInput" />
      </section>
      <!-- 問號圖標 -->
      <router-link :to="{ path: '/guide' }" :class="$style.helpIcon">
        <img alt="Help Icon" src="/help1.svg" />
      </router-link>
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
  .bb {/* Frame上的背景(用於對齊) */
    position: fixed;
    top: 0px;
    left: 0px;
    background-color: var(--color-lavenderblush);
    width: 100%;
    height: 100%;
    display: none;
  }
  .logo1Icon {/* logo */
    position: fixed;
    /* 設定相對位置 */
    height: 19.1%;
    width: 12.5%;
    top: 1%;
    bottom: 99%;
    /* 左右置中操作 */
    left: 50%; /* 讓左邊界在父容器寬度的 50% */
    transform: translateX(-50%); /* 往左平移自身寬度的 50% */
    /* 設定邊界 */
    max-width: 100%;
    max-height: 100%;
    overflow: hidden;/* 超出則隱藏 */
    object-fit: cover;/* 完全填滿其容器 */
    z-index: 3;/* 第三層(最上層) */
  }
  .background {/* contextArea隱藏兒子 */
    align-self: stretch;/* 延伸它爸 */
    height: 93.7%;
    position: relative;
    box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.25);
    border-radius: var(--br-3xs);
    background-color: var(--color-gainsboro);
    display: none;
  }
  .qOutput {/* Q顯示區塊 */
    position: fixed; /* 設定絕對定位 */
    top: 25%;  /* 距離父元素頂部的 25% */
    left: 60%; /* 距離父元素左側的 60% */
    width: 30%;  /* 設定寬度為 30% */
    height: 25%; /* 設定高度為 25% */
    background-color: var(--color-lightcoral);
    border-radius: var(--br-3xs);
    max-width: 100%;
    z-index: 2;
  }
  .qandA {/* QA顯示group */
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-end;
    max-width: 100%;
    height: 100%;
  }
  .aOutput {/* A顯示區塊 */
    position: fixed; /* 設定絕對定位 */
    top: 53%;  /* 距離父元素頂部的 50% */
    left: 10%; /* 距離父元素左側的 15% */
    width: 30%;  /* 設定寬度為 30% */
    height: 25%; /* 設定高度為 25% */
    background-color: var(--color-mistyrose);
    border-radius: var(--br-3xs);
    max-width: 100%;
    z-index: 2;
  }
  .outputArea { /* 輸出格與邊間距 */
    width: 93%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-base);
    max-width: 100%;
  }
  .top {/*標題槓 */
    align-self: stretch;
    height: 18vh;
    position: relative;
    border-radius: var(--br-3xs);
    background-color: var(--color-cadetblue-200);
    z-index: 2;
  }
  .outputAreaWrapper {/* 輸出區塊 */
    align-self: stretch;
    display: flex;
    position: relative;
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
    padding: 0px var(--padding-xl);
    box-sizing: border-box;
    max-width: 100%;
    height: 29vh;
  }
  .questionInput {/* contextArea隱藏二兒子 */
    position: relative;
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: flex-start;
    gap: var(--gap-35xl);
    max-width: 100%;
  }
  .contentArea {/* 禿出來的灰板子 */
    position: fixed;
    /* 留縫 */
    top: 2.5%;
    bottom: 2.5%;
    left: 2%;
    right: 2%;
    /* 加陰影、圓弧、顏色 */
    box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.25);
    border-radius: var(--br-3xs);
    background-color: var(--color-gainsboro);
    /* 板子寬度 */
    width: 96%;
    /* 可當爸 */
    display: flex;
    flex-direction: column;/* 橫向元素排列 */
    align-items: flex-end;/* 垂直居下對齊 */
    justify-content: flex-start;/* 水平居上對齊 */
    padding: 0px 0px var(--padding-25xl);/* 元素內邊距 */
    box-sizing: border-box;/* 控制元素寬度和高度 */
    gap: var(--gap-246xl);/* 設置 flexbox 或 grid 布局中子元素之間間距 */
    max-width: 100%;
    z-index: 1;/* 第一層 */
  }
  .layout {/* Frame上的背景 */
    height: 100%;/* 相對.tapQuest，100%高度 */
    flex: 1;/* 第一層 */
    position: relative;/* 相對定位 */
    background-color: var(--color-lavenderblush);/* 顏色 */
    overflow: hidden;/* 超出則隱藏 */
    max-width: 100%;/* 相對.tapQuest，100%高度 */
  }
  .tapQuest {/* 白色Frame */
    width: 100%;/* 100%寬度 */
    height: 100vh;/* 100vh高度 */
    position: relative;/* 相對定位 */
    display: flex;/* 子元素按此元素排列 */
    flex-direction: row;/* 橫向元素排列 */
    justify-content: center; /* 水平居中對齊 */
    align-items: center; /* 垂直居中對齊 */
    line-height: normal;/* 正常行高 */
    letter-spacing: normal;/* 正常字母間距 */
  }
  .fixedPictureInput {
    position: fixed;   /* 固定在視口中 */
    bottom: 55px;      /* 距離底部 10px */
  }
  .helpIcon {
    position: absolute;
    bottom: 100px;
    left: 100px;
    width: 32px;
    height: 32px;
    cursor: pointer;
    z-index: 4;
  }
  .helpIcon img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  @media screen and (min-width: 1200px) {
    .tapQuest {
      justify-content: space-between; /* 項目之間有間距 */
    }
  }

  @media screen and (min-width: 768px) and (max-width: 1199px) {
    
  }

  @media screen and (max-width: 767px) {
    .tapQuest {
      flex-direction: column; /* 改為縱向排列 */
      height: auto; /* 讓高度自動調整 */
    }
  }
</style>