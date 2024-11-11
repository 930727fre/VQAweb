<template>
  <div class="home">
    <div class="context-input-container">
      <ContextInput />
    </div>
    <div class="image-uploader-container">
      <ImageUploader />
    </div>
  </div>
</template>

<script setup>
import ContextInput from '../components/ContextInput.vue';
import ImageUploader from '../components/ImageUploader.vue'; // 根據實際路徑引入 ImageUploader
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 20px;
}
.context-input-container,
.image-uploader-container {
  margin-top: 100px; /* 可以根據需要調整間距 */
}
</style>




