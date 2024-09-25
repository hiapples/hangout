<script setup>
import { ref } from "vue";

// 滾動容器的引用
const scrollable = ref(null);
const isScrolling = ref(false); // 標記是否正在滾動

// 向左滾動卡片的函數
const scrollLeft = () => {
    if (scrollable.value && !isScrolling.value) {
        const card = scrollable.value.querySelector('.card'); // 獲取第一個卡片
        const cardWidth = card ? card.offsetWidth : 0; // 獲取卡片的寬度
        isScrolling.value = true; // 設置標記，表示開始滾動

        scrollable.value.scrollBy({
            left: -cardWidth, // 向左滾動卡片的寬度
            behavior: 'smooth' // 平滑滾動
        });

        // 在滾動完成後重置標記
        setTimeout(() => {
            isScrolling.value = false;
        },800); // 根據預期的滾動持續時間調整超時持續時間
    }
};

// 向右滾動卡片的函數
const scrollRight = () => {
    if (scrollable.value && !isScrolling.value) {
        const card = scrollable.value.querySelector('.card'); // 獲取第一個卡片
        const cardWidth = card ? card.offsetWidth : 0; // 獲取卡片的寬度
        isScrolling.value = true; // 設置標記，表示開始滾動

        scrollable.value.scrollBy({
            left: cardWidth, // 向右滾動卡片的寬度
            behavior: 'smooth' // 平滑滾動
        });

        // 在滾動完成後重置標記
        setTimeout(() => {
            isScrolling.value = false;
        }, 800); // 根據預期的滾動持續時間調整超時持續時間
    }
};

</script>

<template>
    <div class="scrollable-container" ref="scrollable">
        <div class="d-flex flex-nowrap">
            <div class="col-12">
                <div class="card">Card 1</div>
            </div>
            <div class="col-12">
                <div class="card">Card 2</div>
            </div>
            <div class="col-12">
                <div class="card">Card 3</div>
            </div>
            <div class="col-12">
                <div class="card">Card 4</div>
            </div>
        </div>
    </div>
    <div class="d-flex justify-content-center">
        <button class="bt"@click="scrollLeft" :disabled="isScrolling">上一頁</button>
        <button class="bt ms-3"@click="scrollRight" :disabled="isScrolling">下一頁</button>
    </div>
</template>

<style scoped>
.scrollable-container {
    margin-top: 200px;
    width: 100%;
    height: 600px;
    overflow: hidden; 
}

.row {
    display: flex; /* 保持橫向布局 */
}

.card {
    flex: 0 0 100%; /* 確保每個卡片佔滿容器寬度 */
    height: 570px; /* 卡片高度 */
    background-color: #f8f9fa; /* 便於識別的背景顏色 */
    display: flex;
    align-items: center; /* 垂直居中內容 */
    justify-content: center; /* 水平居中內容 */
}
.bt{
    color: rgb(0, 0, 0); /* 字體顏色 */
    font-size: 24px; /* 字體大小 */
    font-family: 'font';
    background-color: rgb(11, 133, 106);
    padding: 10px 50px;
    cursor: pointer;
    overflow: hidden; /* 確保偽元素不超出範圍 */
    border-radius: 30px;
    border-bottom:  5px solid black;
    border-top:  2px solid black;
    border-left:  2px solid black;
    border-right:  2px solid black;
}
.bt:hover{
    background: linear-gradient(to right, rgb(13, 172, 137), rgb(9, 100, 80));
}
@media (max-width: 992px) {
    .bt{
        font-size: 20px;
    }
}
@media (max-width: 576px) {
    .bt{
        font-size: 16px;
    }
}
</style>
