<template>
    <div class="context-input">
      <h1>Please enter the question </h1>
      <input type="text" v-model="userInput" placeholder="Type something..." />
      <p>You typed: {{ userInput }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  // 定義用於存儲用戶輸入的反應式變數
  const userInput = ref('');
  </script>
  
  <style scoped>
  .context-input {
    text-align: center;
    margin-top: 20px;
  }
  
  input {
    padding: 10px;
    margin: 10px 0;
    font-size: 16px;
    width: 200px;
  }
  </style>
  