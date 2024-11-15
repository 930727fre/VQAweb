<template>
  <div :class="$style.forTypeCharWrapper">
    <div :class="$style.forTypeChar">
      <div :class="$style.charInput" @click="onCharInputClick" />
      <div :class="$style.typeYourQuestion">Type your Question</div>
    </div>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "FrameComponent",
    methods: {
      onCharInputClick() {
        this.$router.push("/tap-quest");
      },
    },
  });
</script>
<style module>
  .charInput {
    position: absolute;
    right: 0px;
    bottom: 0px;
    border-radius: 0px var(--br-3xs) var(--br-3xs) 0px;
    background-color: var(--color-cadetblue-100);
    width: 100%;
    height: 100%;
    cursor: pointer;
  }
  .typeYourQuestion {
    position: absolute;
    right: 490px;
    bottom: 26px;
    display: flex;
    align-items: center;
    width: 232px;
    height: 29px;
    z-index: 1;
  }
  .forTypeChar {
    align-self: stretch;
    height: 81px;
    position: relative;
    z-index: 2;
  }
  .forTypeCharWrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px var(--padding-8xl) 0px 0px;
    box-sizing: border-box;
    min-width: 505px;
    max-width: 100%;
    text-align: left;
    font-size: var(--font-size-5xl);
    color: var(--color-gray);
    font-family: var(--font-roboto);
  }

  @media screen and (max-width: 825px) {
    .forTypeCharWrapper {
      min-width: 100%;
    }
  }
  @media screen and (max-width: 450px) {
    .typeYourQuestion {
      font-size: var(--font-size-lgi);
    }
  }
</style>
