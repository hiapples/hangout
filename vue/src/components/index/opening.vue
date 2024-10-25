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
        }, 3000);
    });
</script>

<template>
    <div v-if="showAnimation" :class="['preload', { 'fade-out': fadeOut }]" >
        <div class="opening-image">
            <div class="d-flex">
                <div class="circle mx-auto"></div>
            </div>
            <p class="text">Hangout</p>
        </div>
    </div>
</template>
    
<style scoped>
    .preload{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color:black;
        z-index: 100;
        display: grid;
        place-content: center;
        justify-items: center;
        transition: opacity 1s ease-out; /* 添加透明度变化的过渡效果 */
    }
    .preload >* {
        transition: 250ms ease; 
    }
    .loaded >* {
        opacity: 0;
    }
    .loaded{
        transition-delay: 250ms;
        transform: translateY(100%);
    }
    .circle{
        width: clamp(50px, 10vw + 20px, 112px);
        height: clamp(50px, 10vw + 20px, 112px);
        border-radius: 50%;
        border: 3px solid rgb(167, 167, 167);
        border-block-start-color: rgb(0, 0, 0);
        margin-block-end: 45px;
        animation: rotate360 1s linear infinite;
    }
    @keyframes rotate360{
        0%{transform: rotate(0);}
        100%{transform: rotate(1turn);}
    }
    .text {
        background-image: linear-gradient(90deg,transparent 0% 16.66% ,rgb(9, 101, 81) 33.33% 50% , transparent 66.66% 75%);
        background-size: 500%;
        font-size: calc(2rem + 3vw);
        font-family: 'font2';
        font-weight: 700;
        line-height: 1em;
        text-transform: uppercase;
        letter-spacing: 16px;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-stroke: 0.5px rgb(9, 101, 81);
        animation: loadingText linear 2s infinite;
    }

    @keyframes loadingText{
        0%{background-position: 100%;}
        100%{background-position: 0%;}
    }

    .opening-image {
        animation: fadeIn 2s ease-out forwards;
    }

    .fade-out {
        opacity: 0; /* 设置退出时透明度为 0 */
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }
</style>
