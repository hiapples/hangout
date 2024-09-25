<script setup>
import { ref } from "vue";

// 滾動容器的引用
const scrollable = ref(null);
const isScrolling = ref(false); // 標記是否正在滾動
const activeCard = ref(0); // 追踪當前活躍的卡片索引
const totalCards = 4; // 總卡片數量

// 向左滾動卡片的函數
const scrollLeft = () => {
    if (scrollable.value && !isScrolling.value && activeCard.value > 0) {
        const card = scrollable.value.querySelector('.card'); // 獲取第一個卡片
        const cardWidth = card ? card.offsetWidth : 0; // 獲取卡片的寬度
        isScrolling.value = true; // 設置標記，表示開始滾動

        scrollable.value.scrollBy({
            left: -cardWidth, // 向左滾動卡片的寬度
            behavior: 'smooth' // 平滑滾動
        });

        // 在滾動完成後更新活躍卡片索引
        activeCard.value--; // 僅在卡片不在第一個時減少索引

        // 在滾動完成後重置標記
        setTimeout(() => {
            isScrolling.value = false;
        }, 500); // 根據預期的滾動持續時間調整超時持續時間
    }
};

// 向右滾動卡片的函數
const scrollRight = () => {
    if (scrollable.value && !isScrolling.value && activeCard.value < totalCards - 1) {
        const card = scrollable.value.querySelector('.card'); // 獲取第一個卡片
        const cardWidth = card ? card.offsetWidth : 0; // 獲取卡片的寬度
        isScrolling.value = true; // 設置標記，表示開始滾動

        scrollable.value.scrollBy({
            left: cardWidth, // 向右滾動卡片的寬度
            behavior: 'smooth' // 平滑滾動
        });

        // 在滾動完成後更新活躍卡片索引
        activeCard.value++; // 僅在卡片不在最後一個時增加索引

        // 在滾動完成後重置標記
        setTimeout(() => {
            isScrolling.value = false;
        }, 500); // 根據預期的滾動持續時間調整超時持續時間
    }
};
</script>


<template>
    <div id="carouselExampleIndicators" class="carousel slide " >
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner" id="title-section2">
            <div class="carousel-item active">
                <div class="card">
                    <div class="card-head">
                        <div class="card-head-inner">
                            活動消息
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="card-body-inner ">
                            <div class="news-title mt-2">
                                //PANGCAH生活節//<br/>
                                日期：9/7、8<br/>
                                地點：大農大富
                            </div>
                            <br/>
                            <div class="news-body">
                                #漢堡製藥所
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="carousel-item">
                <div class="card">
                    <div class="card-head">
                        <div class="card-head-inner">
                            營運消息
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="card-body-inner ">
                            <div class="news-title mt-2">
                                九月休假/SeptemberOffDay<br/>
                                1/2/9/15/16/22/23/29/30<br/>
                            </div>
                            <br/>
                            <div class="news-body">
                                哪有人活著是容易的，<br/>
                                只是<br/>
                                每個人都在“不動聲色的努力著”。<br/>
                                對我們來說<br/>
                                “味道”  她沒有真正的 定義，<br/>
                                但  她會延伸出我們的 生活品味，<br/>
                                跟我們 看事情 的方法。<br/>
                                如果您也喜歡，我們很開心。<br/>
                                我們知道 我們不會是最好的 那一個，<br/>
                                但我們 絕對是最努力的那 兩個。<br/>
                                #漢堡製藥所
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="carousel-item">
                <div class="card">
                    <div class="card-head">
                        <div class="card-head-inner">
                            營運消息
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="card-body-inner ">
                            <div class="news-title mt-2">
                                八月休假/AugustOffDay<br/>
                                4/5/11/12/18/19/20/21/22/23/24/25/26<br/>
                            </div>
                            <br/>
                            <div class="news-body">
                                雖然花蓮光觀受到影響...<br/>
                                但我們不想停下腳步，<br/>
                                造船的目的從來不是停在港灣，<br/>
                                而是衝擊風浪。<br/>
                                7月我們進行了些許裝修，<br/>
                                把店面跟我們自己調整好，<br/>
                                迎接隨時可能會來訪的你們。<br/>
                                只有足夠努力，才會足夠幸運。<br/>
                                #漢堡製藥所
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
#carouselExampleIndicators {
    margin-top: 150px;
    width: 100%;
    height: 650px;
    overflow: hidden; 
}
.row {
    display: flex; /* 保持橫向布局 */
}
.news-title{
    color: rgb(190, 4, 4);
    font-size: 18px;
    padding: 0px 10px;
}
.news-body{
    line-height: 1.8;
    font-size: 16px;
}
.card-head-inner{
    background-color: rgb(164, 185, 180);
    text-align: center;
    font-size: 30px;
    font-family: 'font';
    padding: 20px 0px;
}
.card-head{
    border: 5px solid rgb(164, 185, 180);
    padding:10px;
    margin: 20px;
}
.card-body-inner{
    background-color: rgb(164, 185, 180);
    text-align: center;
    font-family: 'font';
    padding: 20px 10px;
    height: 465px;
}
.card-body{
    border: 5px solid rgb(164, 185, 180);
    padding:10px;
    margin: 0px 20px 20px 20px;
}
.card {
    flex: 0 0 100%; /* 確保每個卡片佔滿容器寬度 */
    height: 670px; /* 卡片高度 */
    background-color: #f8f9fa; /* 便於識別的背景顏色 */
    display: flex;
    border-radius: 0%;
}


@media (max-width: 992px) {

}
@media (max-width: 576px) {
    .news-title{
        font-size: 16px;
    }
    .news-body{
        font-size: 14px;
    }
}
</style>
