<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const isScrolled = ref(false);
const isHidden = ref(false);
let lastScrollY = window.scrollY;

// 設定一個閾值，避免滾動時的微小誤差
const SCROLL_THRESHOLD = 5;

// 滾動事件處理
const handleScroll = () => {
  const currentScrollY = window.scrollY;

  // 當滾動高度小於閾值時，視為已滾動到頂部
  if (currentScrollY <= SCROLL_THRESHOLD) {
    isHidden.value = false; // 顯示導航欄
    return; // 結束函數，不執行後續隱藏邏輯
  }

  // 超過50px滾動時改變導航狀態
  isScrolled.value = currentScrollY > 50;

  // 向下滾動時隱藏導航，向上滾動顯示導航
  if (currentScrollY > lastScrollY) {
    isHidden.value = true; // 向下滾動，隱藏導航
  } else {
    isHidden.value = false; // 向上滾動，顯示導航
  }

  lastScrollY = currentScrollY;
};




// 滾動到指定部分的函數，滾完畢後隱藏導航
const scrollToSection = (index) => {
  const targetSectionId = `title-section${index + 1}`;
  const targetSection = document.getElementById(targetSectionId);
  
  if (targetSection) {
    const offsetPosition = targetSection.getBoundingClientRect().top + window.scrollY - 50;

    window.scrollTo({
      top: offsetPosition,
      behavior: 'smooth',
    });

    // 使用 setInterval 檢測滾動是否完成
    const checkIfScrollFinished = setInterval(() => {
      if (Math.abs(window.scrollY - offsetPosition) < 1) { // 檢查滾動是否到達目標
        clearInterval(checkIfScrollFinished);

        // 滾動完畢後隱藏導航
        isHidden.value = true;
      }
    }, 100); // 每 100 毫秒檢查一次滾動是否完成
  }
};



// 註冊和取消滾動事件
onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>
<template>
  <!-- nav -->
  <nav :class="['navbar', 'navbar-expand-lg', isScrolled ? 'navbar-colored' : 'navbar-transparent', { hidden: isHidden }]">
    <div class="container-fluid">
      <a class="navbar-brand" href="all.php">
        <img src="/src/photo/logo2.png" width="250" />
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item me-lg-3 ms-lg-0 ms-auto">
            <button class="nav-link" aria-current="page" @click="scrollToSection(0)">關於我們</button>
          </li>
          <li class="nav-item me-lg-3 ms-auto">
            <button class="nav-link">最新消息</button>
          </li>
          <li class="nav-item me-lg-3 ms-auto">
            <button class="nav-link">菜單</button>
          </li>
          <li class="nav-item me-lg-3 ms-auto">
            <button class="nav-link">登入</button>
          </li>
          <li class="nav-item me-lg-3 ms-auto">
            <button class="nav-link">聯絡我們</button>
          </li>
        </ul>
      </div>
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

.hidden {
  transform: translateY(-100%); 
}

.navbar-transparent {
  background-color: transparent;
  transition: background-color 0.5s ease;
}

.navbar-colored {
  background-color: rgba(41, 41, 41, 0.9); /* 修改为你想要的颜色 */
  transition: background-color 0.5s ease;
  opacity: 1;
}

.navbar-toggler {
  background-color: #ffffff; /* 或者你想要的任何顏色 */
  opacity: 0.3; /* 確保不透明 */
}

.nav-item {
  font-family: 'font';
}

.nav-link {
  color: #ffffff;
  font-size: 18px;
  border-radius: 20px;
}

.nav-link:hover {
  color: rgb(11, 133, 106);
  animation: bounce 0.8s; /* 添加跳動動畫 */
  border-radius: 20px;
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px); /* 向上移動的距離 */
  }
}

@media (max-width: 992px) {
  .nav-item button {
    text-align: end;
  }
  .nav-link:hover {
    color: white;
    background-color: transparent;
    padding: 8px 0px;
    animation: none;
  }
}

@media (max-width: 576px) {
  .nav-item button {
    font-size: 14px;
  }
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
