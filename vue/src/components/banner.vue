<script setup>
import { ref } from "vue";
import { onMounted, onUpdated, onUnmounted } from "vue";


// 滾動到指定部分的函數
const scrollToSection = (index) => {
  const targetSectionId = `title-section${index + 1}`; // 確保這個 ID 存在
  const targetSection = document.getElementById(targetSectionId);
  if (targetSection) {
    const offsetPosition = targetSection.getBoundingClientRect().top + window.scrollY - 50;
    window.scrollTo({
      top: offsetPosition,
      behavior: 'smooth',
    });
  }
};
</script>

<template>
    <div class="image-container">
        <img class="Banner" src="../photo/banner1.jpg" alt="Banner">
        <div class="subtitle">加入會員</div>
        <div class="subtitle2">關注我們獲得最新消息</div>
        <img class="down" src="../photo/down.png" @click="scrollToSection(0)">
    </div>
</template>

<style scoped>
.image-container {
    width: 100%;
    height: 800px; /* 根据需要调整高度 */
    overflow: hidden; /* 隐藏超出容器的部分 */
    position: relative;
}
.Banner{
    width: 100%;
    height: 100%; /* 确保图片填充容器高度 */
    object-fit: cover; /* 保持图片比例并填充容器 */
    object-position: center; /* 图片居中显示 */
}
.down{
    position: absolute;
    top: 82%; /* 垂直居中 */
    left: 50%; /* 水平居中 */
    transform: translate(-50%, -50%); /* 精確居中 */
    width: 50px;
    cursor: pointer;
}
.subtitle2{
    position: absolute;
    top: 72%; /* 垂直居中 */
    left: 50%; /* 水平居中 */
    transform: translate(-50%, -50%); /* 精確居中 */
    color: rgb(255, 255, 255); /* 字體顏色 */
    font-size: 20px; /* 字體大小 */
    font-family: 'font';
    transition: transform 0.3s ease; /* 添加過渡效果 */
}
.subtitle:hover + .subtitle2 {
    transform: translate(-50%, 0); /* 懸停時靠近並水平居中 */
}

.subtitle{
    position: absolute;
    top: 62%; /* 垂直居中 */
    left: 50%; /* 水平居中 */
    transform: translate(-50%, -50%); /* 精確居中 */
    color: rgb(0, 0, 0); /* 字體顏色 */
    font-size: 24px; /* 字體大小 */
    font-family: 'font';
    background-color: rgb(11, 133, 106);
    padding: 10px 50px;
    box-sizing: border-box; /* 包含內邊距 */
    outline: 7px solid rgb(11, 133, 106); /* 外框，與本體保持距離 */
    outline-offset: 7px; /* 外框距離本體 10px */
    cursor: pointer;
    transition: outline-offset 0.5s, border-radius 0.25s,outline-color 0.5s; /* 過渡效果 */
    overflow: hidden; /* 確保偽元素不超出範圍 */
}
.subtitle:hover{
    outline-offset: 0px;
    border-radius: 20px;
    outline-color: rgba(11, 133, 106, 0);
    background: linear-gradient(to right, rgb(13, 172, 137), rgb(9, 100, 80));
}
.subtitle::before {
    content: ''; /* 必須設置內容才能顯示偽元素 */
    position: absolute;
    top: 0;
    left: -100%; /* 初始位置在左側之外 */
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.5); /* 白色光影，透明度為 0.5 */
    transition: left 0.3s ease; /* 動畫持續時間和效果 */
}

.subtitle:hover::before {
    left: 100%; /* 滑鼠懸停時，白光從左到右移動 */
}
@media (max-width: 576px) {
    .subtitle{
        font-size: 20px;
    }
    .subtitle2{
        font-size: 16px;
    }
}
</style>
