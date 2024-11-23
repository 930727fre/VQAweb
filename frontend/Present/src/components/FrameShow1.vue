<template>
  <div :class="$style.rectangleParent">
    <div :class="$style.frameChild" />
    <div :class="$style.theWordsYouContainer">
      <p :class="$style.theWords">The words you input will show</p>
      <p :class="$style.atRightside">at rightside.</p>
    </div>
    <div :class="$style.theAnswerGivenByTheSystemParent">
      <div :class="$style.theAnswerGivenContainer">
        <p :class="$style.atRightside">The answer given by the system</p>
        <p :class="$style.atRightside">show at left.</p>
      </div>
      <div :class="$style.theAnswerGivenContainer">Press next to move on.</div>
    </div>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "FrameShow1",
    methods: {
      onNextButtonContainerClick() {
         // 跳转到名为 'GuideShow' 的路由
        this.$router.push("/guide-show");
      },
    },
  });
</script>
<style module>
  .frameChild {
    width: 520px;
    height: 257px;
    position: relative;
    background-color: var(--color-gainsboro-100);
    display: none;
    max-width: 100%;
  }
  .theWords {
    margin: 0;
    white-space: pre-wrap;
  }
  .atRightside {
    margin: 0;
  }
  .theWordsYouContainer {
    position: relative;
    display: inline-block;
    max-width: 100%;
    z-index: 3;
  }
  .theAnswerGivenContainer {
    position: relative;
    z-index: 3;
  }
  .theAnswerGivenByTheSystemParent {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-3xl);
    max-width: 100%;
  }
  .rectangleParent {
    position: absolute;
    top: 546px;
    left: 920px;
    background-color: var(--color-gainsboro-100);
    width: 520px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-2xl) var(--padding-35xl) var(--padding-14xl);
    box-sizing: border-box;
    gap: var(--gap-22xl);
    max-width: 100%;
    z-index: 2;
    text-align: left;
    font-size: var(--body-size);
    color: var(--color-black);
    font-family: var(--body);
  }

  @media screen and (max-width: 450px) {
    .theWordsYouContainer {
      font-size: var(--font-size-lgi);
    }

    .theAnswerGivenContainer {
      font-size: var(--font-size-lgi);
    }
  }
</style>
