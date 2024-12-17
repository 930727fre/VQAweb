<template>
  <div :class="$style.result">
    <img :class="$style.logo1Icon" alt="" src="/logo-1@2x.png" />
    <img :class="$style.HomeButtom" @click="onResultContainerClick" alt="" src="/home_buttom.png" />
    <main :class="$style.layout">
      <div :class="$style.bb" />
      <section :class="$style.frameParent">
        <div :class="$style.backgroundParent">
          <div :class="$style.background" />
          <header :class="$style.top" />
          <div :class="$style.outputArea">
            <!-- 顯示 question -->
            <div :class="$style.qOutput">
              {{ question }}
              <!-- 圖片預覽 -->
              <div v-if="image" class="image-preview">
                <img :src="image" alt="Uploaded Preview" />
              </div>
            </div>
            <!-- 顯示 answer -->
            <section :class="$style.aOutput">
              {{ answer }}
            </section>
          </div>
        </div>
        <img :class="$style.sendIcon" loading="lazy" alt="" src="/send.svg" />
      </section>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useRoute, useRouter } from "vue-router";  // 引入 useRoute 和 useRouter

export default defineComponent({
  name: "Result",
  setup() {
    const router = useRouter(); 
    const route = useRoute();  // 使用 useRoute 來取得當前路由資訊

    // 從路由的 query 參數中取得 question 和 image
    const question = route.query.question as string || '';  // 取得問題內容
    const image = route.query.image as string || '';  // 取得圖片資料
    const answer = route.query.answer as string || 'No result.'; // 取得答案
    // 點擊時，跳轉回首頁
    const onResultContainerClick = () => {
      router.push("/");  // 跳轉到首頁
    };

    return {
      question,
      answer,
      image,
      onResultContainerClick
    };
  },
});
</script>

<style scoped>
.image-preview {
  margin-top: 1.3%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-preview img {
  max-width: 60.8%; /* 限制圖片的最大寬度 */
  max-height: 37%; /* 限制圖片的最大高度 */
  width: auto; /* 確保寬高比例 */
  height: auto; /* 確保寬高比例 */
  object-fit: contain; /* 保持圖片內容完整可見 */
}
</style>
<style module>
  .bb {
    position: fixed;
    top: 0px;
    left: 0px;
    background-color: var(--color-lavenderblush);
    width: 100%;
    height: 100%;
    display: none;
  }
  .background {
    align-self: stretch;/* 延伸它爸 */
    height: 93.7%;
    position: relative;
    box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.25);
    border-radius: var(--br-3xs);
    background-color: var(--color-gainsboro);
    display: none;
  }
  .top {
    align-self: stretch;
    height: 18vh;
    position: relative;
    border-radius: var(--br-3xs);
    background-color: var(--color-cadetblue-200);
    min-height: 18vh;
    z-index: 2;
  }
  .aOutput {
    position: fixed; /* 設定絕對定位 */
    top: 53%;  /* 距離父元素頂部的 50% */
    left: 10%; /* 距離父元素左側的 15% */
    width: 35%;  /* 設定寬度為 30% */
    min-height: 25%; /* 設定高度為 25% */
    max-height : 35%;
    background-color: var(--color-mistyrose);
    border-radius: var(--br-3xs);
    max-width: 100%;
    z-index: 2;
    font-family: 'Arial', sans-serif;
    font-size: 1.5vw;
    color: #04010e;
    padding: 0.5%;
    overflow-y: auto;
    overflow-wrap: break-word;
    word-wrap: break-word;
    white-space: pre-wrap;
    margin-bottom: 0.5%;
  }
  /* question 的字體樣式 */
  .qOutput {
    position: fixed; /* 設定絕對定位 */
    top: 25%;  /* 距離父元素頂部的 25% */
    left: 55%; /* 距離父元素左側的 60% */
    width: 35%;  /* 設定寬度為 30% */
    background-color: var(--color-lightcoral);
    border-radius: var(--br-3xs);
    max-width: 100%;
    max-height : 45%;
    z-index: 2;
    font-family: 'Arial', sans-serif;
    font-size: 1.5vw;
    color: #04010e;
    padding: 0.5%;
    overflow-y: auto;
    overflow-wrap: break-word;
    word-wrap: break-word;
    margin-bottom: 0.5%;
  }
  .sendIcon {
    position: fixed;
    right: 4.5%;
    bottom: 4.7%;
    width: 8%;
    height: 8%;
    overflow: hidden;
    z-index: 4;
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
  .backgroundParent {
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
  .logo1Icon {
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
    object-fit: contain;/* 完全填滿其容器 */
    z-index: 3;/* 第三層(最上層) */
  }
  .HomeButtom {
    position: fixed;
    /* 設定相對位置 */
    height: 10%;
    width: 4%;
    top: 6%;
    bottom: 94%;
    /* 左右置中操作 */
    left: 15%;
    /* 讓左邊界在父容器寬度的 50% */
    transform: translateX(-85%);
    /* 往左平移自身寬度的 50% */
    /* 設定邊界 */
    max-width: 100%;
    max-height: 100%;
    overflow: hidden;
    /* 超出則隱藏 */
    object-fit: contain;
    /* 完全填滿其容器 */
    z-index: 3;
    /* 第三層(最上層) */
  }
  .frameParent {
    height: 96%;
    flex: 1;
    position: relative;
    max-width: 100%;
  }
  .layout {/* Frame上的背景 */
    height: 100%;/* 相對.tapQuest，100%高度 */
    flex: 1;/* 第一層 */
    position: relative;/* 相對定位 */
    background-color: var(--color-lavenderblush);/* 顏色 */
    overflow: hidden;/* 超出則隱藏 */
    max-width: 100%;/* 相對.tapQuest，100%高度 */
  }
  .result {
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

  @media screen and (min-width: 1200px) {
    .result {
      justify-content: space-between; /* 項目之間有間距 */
    }
  }

  @media screen and (min-width: 768px) and (max-width: 1199px) {
    .qOutput{
      font-size: 3.5vw;
    }
    .aOutput{
      font-size: 3.5vw;
    }
    .logo1Icon {/* logo */
      transform: translateX(-50%) scale(2); /*放大logo比例*/
    }
    .HomeButtom{
      transform: translateX(-80%) scale(2); /*放大logo比例*/
    } 
  }

  @media screen and (max-width: 767px) {
    .result {
      flex-direction: column; /* 改為縱向排列 */
      height: auto; /* 讓高度自動調整 */
    }
    .qOutput{
      font-size: 4.5vw;
    }
    .aOutput{
      font-size: 4.5vw;
    }
    .logo1Icon {/* logo */
      transform: translateX(-50%) scale(3); /*放大logo比例*/
    }
    .HomeButtom {
      transform: translateX(-80%) scale(3);
      /*放大logo比例*/
    }
  }
</style>


