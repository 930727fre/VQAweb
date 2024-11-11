<template>
    <div class="image-uploader">
      <h1>Please upload an image</h1>
      <input type="file" @change="onFileChange" accept="image/*" />
      <div v-if="imageUrl">
        <img :src="imageUrl" alt="Please upload an image:" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        imageUrl: null,
      };
    },
    methods: {
      onFileChange(event) {
        const file = event.target.files[0];
        if (file && file.type.startsWith('image/')) {
          this.imageUrl = URL.createObjectURL(file);
        } else {
          alert('Please upload a valid image file.');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .image-uploader {
    text-align: center;
  }
  .image-uploader h2 {
    margin-bottom: 1rem; /* 可以調整標題的底部邊距 */
  }
  .image-uploader img {
    max-width: 100%;
    height: auto;
  }
  </style>
  