<template>
  <section :class="$style.instructionsContainerParent">
    <div :class="$style.instructionsContainer">
      <div :class="$style.instructionBlock">
        <div :class="$style.rectangleParent">
          <div :class="$style.frameChild" />
          <div :class="$style.uploadThePicutures">
            Upload the picutures lefthand side.
          </div>
          <div :class="$style.uploadThePicutures">
            Upload the texts righthand side.
          </div>
          <div :class="$style.pressNextTo">Press next to move on.</div>
        </div>
        <NextButton
          property1="Next1"
          nextButtonPosition="relative"
          nextButtonTop="unset"
          nextButtonLeft="unset"
          :onNextButtonContainerClick="onNextButtonContainerClick"
        />
      </div>
    </div>
    <div :class="$style.imageInputParent">
      <div :class="$style.imageInput">
        <div :class="$style.forInputPic">
          <div :class="$style.picInput" />
          <div :class="$style.body">Upload the picture</div>
        </div>
      </div>
      <div :class="$style.forTypeChar">
        <div :class="$style.charInput" />
        <div :class="$style.body">Type your Question</div>
      </div>
      <div :class="$style.sendButtonContainer">
        <img :class="$style.sendIcon" loading="lazy" alt="" src="/send1.svg" />
      </div>
    </div>
  </section>
</template>
<script lang="ts">
  import { defineComponent } from "vue";
  import NextButton from "./NextButton.vue";

  export default defineComponent({
    name: "FrameComponent2",
    components: { NextButton },
    methods: {
      onNextButtonContainerClick() {
        this.$router.push("/normal");
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
  .uploadThePicutures {
    position: relative;
    display: inline-block;
    max-width: 100%;
    z-index: 3;
  }
  .pressNextTo {
    position: relative;
    z-index: 3;
  }
  .rectangleParent {
    flex: 1;
    background-color: var(--color-gainsboro-100);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-16xl) var(--padding-xl) var(--padding-14xl)
      var(--padding-35xl);
    box-sizing: border-box;
    gap: var(--gap-33xl-5);
    min-width: 338px;
    max-width: 100%;
    z-index: 2;
  }
  .instructionBlock {
    width: 776px;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: flex-start;
    flex-wrap: wrap;
    align-content: flex-end;
    gap: var(--gap-13xl);
    max-width: 100%;
  }
  .instructionsContainer {
    width: 978px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
    padding: 0px var(--padding-xl);
    box-sizing: border-box;
    max-width: 100%;
  }
  .picInput {
    height: 81px;
    width: 750px;
    position: relative;
    border-radius: var(--br-3xs) 0px 0px var(--br-3xs);
    background-color: var(--color-skyblue);
    display: none;
    max-width: 100%;
  }
  .body {
    width: 232px;
    position: relative;
    display: flex;
    align-items: center;
    flex-shrink: 0;
    z-index: 1;
  }
  .forInputPic {
    align-self: stretch;
    border-radius: var(--br-3xs) 0px 0px var(--br-3xs);
    background-color: var(--color-skyblue);
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-7xl) var(--padding-11xl);
    box-sizing: border-box;
    max-width: 100%;
    z-index: 2;
  }
  .imageInput {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px var(--padding-5xl) 0px 0px;
    box-sizing: border-box;
    min-width: 503px;
    max-width: 100%;
  }
  .charInput {
    height: 81px;
    width: 750px;
    position: relative;
    border-radius: 0px var(--br-3xs) var(--br-3xs) 0px;
    background-color: var(--color-cadetblue-100);
    display: none;
    max-width: 100%;
  }
  .forTypeChar {
    width: 750px;
    border-radius: 0px var(--br-3xs) var(--br-3xs) 0px;
    background-color: var(--color-cadetblue-100);
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-7xl) var(--padding-9xl);
    box-sizing: border-box;
    max-width: 100%;
    z-index: 2;
  }
  .sendIcon {
    width: 74px;
    height: 74px;
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
    z-index: 2;
  }
  .sendButtonContainer {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px 0px var(--padding-10xs);
  }
  .imageInputParent {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: center;
    flex-wrap: wrap;
    align-content: flex-end;
    gap: var(--gap-8xl);
    max-width: 100%;
    color: var(--color-gray);
  }
  .instructionsContainerParent {
    position: absolute;
    top: 546px;
    left: 145px;
    width: 1652px;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: flex-start;
    gap: var(--gap-66xl);
    max-width: 100%;
    text-align: left;
    font-size: var(--body-size);
    color: var(--color-black);
    font-family: var(--body);
  }

  @media screen and (max-width: 625px) {
    .imageInput {
      min-width: 100%;
    }
  }
  @media screen and (max-width: 450px) {
    .uploadThePicutures {
      font-size: var(--font-size-lgi);
    }

    .pressNextTo {
      font-size: var(--font-size-lgi);
    }

    .rectangleParent {
      min-width: 100%;
    }

    .body {
      font-size: var(--font-size-lgi);
    }
  }
</style>
