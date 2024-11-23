<template>
  <div :class="$style.frameArrow" :data-property1="property1">
    <div :class="$style.arow1">
      <img :class="$style.vectorIcon" loading="lazy" alt="" src="/vector.svg" />
      <img :class="$style.vectorIcon1" alt="" src="/vector-1.svg" />
    </div>
    <div :class="$style.arow2">
      <img :class="$style.vectorIcon2" alt="" src="/vector.svg" />
      <img :class="$style.vectorIcon3" alt="" src="/vector-1.svg" />
    </div>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "FrameArrow",
    props: {
      property1: { type: Number, default: 1 },
    },
  });
</script>
<style module>
  .vectorIcon {
    height: 17.9px;
    width: 7.5px;
    position: relative;
    object-fit: contain;
  }
  .vectorIcon1 {
    height: 17.9px;
    width: 7.5px;
    position: relative;
    object-fit: contain;
  }
  .arow1 {
    margin-left: -32.9px;
    height: 23.9px;
    width: 20.9px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    z-index: 2;
  }
  .vectorIcon2 {
    height: 17.9px;
    width: 7.5px;
    position: relative;
    object-fit: contain;
  }
  .vectorIcon3 {
    height: 17.9px;
    width: 7.5px;
    position: relative;
    object-fit: contain;
  }
  .arow2 {
    height: 23.9px;
    width: 20.9px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    z-index: 1;
  }
  .frameArrow {
    width: 20.9px;
    height: 23.9px;
    overflow: hidden;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-xs);
  }
</style>
