<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const isVisible = ref(false);

const handleScroll = () => {
    isVisible.value = window.scrollY > 100;
};

const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};

onMounted(() => {
    window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
    window.removeEventListener("scroll", handleScroll);
});
</script>

<template>
    <div class="back-container">
        <a :class="['back-value', { 'show': isVisible }]" href="#" @click.prevent="scrollToTop" id="toTopBtn">TOP</a>
    </div>
</template>

<style scoped>
.back-container {
    position: relative;        
}

.back-value {
    position: fixed;
    right: 25px;
    bottom: 30px;
    padding: 10px 7px; 
    border-radius: 50%; 
    color:  rgb(9, 79, 64);
    border: 3px solid rgb(9, 79, 64);
    font-family: 'font';
    text-decoration: none;
    opacity: 0; /* 開始時隱藏 */
    transition: opacity 1.5s ease, background-color 0.5s; /* 添加過渡效果 */
    pointer-events: none; /* 不接收點擊事件 */
    z-index: 99;
}

.back-value.show {
    opacity: 1; /* 顯示時 */
    pointer-events: auto; /* 允許點擊事件 */
}

.back-value:hover {
    background-color: rgb(11, 133, 106);
    color: black;
}

@media (max-width: 992px) {
    .back-value {
        right: 10px;
        bottom: 20px;
        padding: 7px 4px; 
        font-size: 14px;
    }
}
</style>
