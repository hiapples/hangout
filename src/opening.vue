<script setup>
    import { ref } from "vue";
    import { onMounted } from "vue";
    const showAnimation = ref(true);
    const fadeOut = ref(false);

    onMounted(() => {
        setTimeout(() => {
            fadeOut.value = true;
            setTimeout(() => {
                showAnimation.value = false;
            }, 300);
        }, 2600);
    });
</script>

<template>
    <div>
        <div v-if="showAnimation" :class="['intro-animation', { 'fade-out': fadeOut }]" id="intro-animation">
            <img src="/src/photo/logo2.png" class="opening-image">
        </div>
    </div>
</template>

<style scoped>
    body {
        margin: 0;
    }

    .intro-animation {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 10000000000000000; /* 确保动画在顶层显示 */
        background-color: #fff;
        transition: opacity 1s ease-out; /* 添加透明度变化的过渡效果 */
    }

    .opening-image {
        width: 50%; /* 调整图片大小 */
        animation: fadeIn 2s ease-out forwards;
    }

    .fade-out {
        opacity: 0; /* 设置退出时透明度为 0 */
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
            transform: scale(0.8);
        }
        100% {
            opacity: 1;
            transform: scale(1);
        }
    }
</style>
