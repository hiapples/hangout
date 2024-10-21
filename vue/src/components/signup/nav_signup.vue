<script setup>
import { ref, onMounted, onUnmounted } from "vue";


</script>
<template>
  <!-- nav -->
  <nav class="navbar">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">
        <img src="../../photo/logo2.png" width="250" />
      </a>
    </div>
  </nav>
</template>
<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 10000000; /* 確保導航欄在所有內容之上 */
  padding: 10px;
  transition: transform 0.5s ease !important; /* 平滑過渡 */
}
@media (max-width: 576px) {
  img {
    width: 200px;
  }
}
@font-face {
  font-family: 'font';
  src: url('/src/fonts/font.otf') format('opentype');
  font-weight: normal;
  font-style: normal;
}
</style>
