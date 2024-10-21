<script setup>
import { ref } from "vue";
import { onMounted,onUpdated,onUnmounted } from "vue";

const isFlipped = ref(false);
const isTransparent = ref(false);

function change() {
    isTransparent.value = true; // 開始翻轉，設為透明
    setTimeout(() => {
        isFlipped.value = !isFlipped.value; // 翻轉
    }, 200); // 在翻轉動畫持續時間後執行
    setTimeout(() => {
        isTransparent.value = false; // 翻轉後恢復不透明
    }, 1200); // 恢復顏色
}

const fadeInElement = ref(null);
const fadeInElement2 = ref(null);
onMounted(() => {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    });

    if (fadeInElement.value) {
        observer.observe(fadeInElement.value);
    }
    if (fadeInElement2.value) {
        observer.observe(fadeInElement2.value);
    }
});
</script>

<template>
    <div class="container">
        <div class="row d-flex g-0">
            <div class="col-11 col-lg-5 mb-5 mb-lg-0 mx-auto bc2 card" ref="fadeInElement" @click="change" :class="{ transparent: isTransparent }">
                <div class="flip-card-inner" :class="{ flipped: isFlipped }"  >
                    <div class="inner-content">
                        <div class="flip-card-front">
                            <div id="title-section1" class="title text-center">從餐車到店面</div>
                            <div class="subtitle text-center">
                                座位有限小吃部<br/>
                                我會想念街道生活中，不期而遇的溫暖<br/>
                                也會銘記大雨滂沱，沒有傘的日子<br/>
                                Kiciyang慶降是餐車<br/>也是你們各位常Hang Out的地點<br/>
                                所以店面，我們取名為:Hang Out<br/>
                                <br/>
                                這裡感謝很多我們身邊的朋友們<br/>
                                鼎力協助許多店裡的大小事務<br/>
                                哪怕是一杯飲料、一根螺絲，我們都感恩在心<br/>
                                <br/>
                                嘿，各位，那些年來<br/>
                                與我們一起在街道上的朋友們，接下來<br/>
                                我們要用店面描繪心中生活的樣子<br/>
                                用食物敘述我們生活中想要的節奏<br/>
                                <br/>
                                ||:HANG OUT ||雅座/立食/外帶店<br/>
                                花蓮在地 特有種”檳榔綠
                            </div>
                        </div>
                        <div class="flip-card-back">
                            <div class="title text-center">序≒續</div>
                            <div class="subtitle text-center">
                                為了實踐我自己幻想中的樣子<br/>
                                這7年來街道生活給了我大大小小的考驗<br/>
                                ””生活不是等待暴風雨過去<br/>
                                而是學會在雨中翩翩起舞””<br/>
                                <br/>
                                餐車  配上  街道<br/>
                                煎鏟碰撞出的聲響<br/>
                                洞悉此刻出餐該有怎樣的節奏<br/>
                                爐台上的食物<br/>
                                藉由梅納反應所產生的樂曲<br/>
                                <br/>
                                ”慶降Kiciyang”對我來說是一種生活的精神象徵<br/>
                                用自己喜歡的方式好好活著<br/>
                                <br/>
                                就算忙碌後<br/>
                                ”鏡子反射自己狼狽的模樣<br/>
                                都讓我覺得莫名的浪漫.......
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-11 col-lg-5 card mx-auto bc" ref="fadeInElement2">
                <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel" >
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="../../photo/content1.jpg" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                            <img src="../../photo/content2.jpg" class="d-block w-100" alt="...">
                        </div>
                        <div class="carousel-item">
                            <img src="../../photo/content3.jpg" class="d-block w-100" alt="...">
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-12" >
                <div class="text-container">
                    <div>
                        <img class="hb" src="../../photo/banner1.jpg"/>
                    </div>
                    <div>
                        <img class="icon-fork" src="../../photo/fork.png"/>
                    </div>
                    <div class="text-inner d-flex align-items-center">
                        顧客們的好評推薦，我們持續求新求變。<br>
                        以最新鮮的食材為基調，漢堡結合各項特色風味，豐富您的味蕾體驗。<br>
                        在這裡，您可以享受各式漢堡、熱狗，搭配精選啤酒，隨興小酌，與美味佳餚一同度過美好時光。<br>
                        因為對食物的熱愛，我們與顧客們建立了深厚的感情，這也是我們不斷進步的原動力。
                    </div>
                    <div class="icon-bg"></div>
                </div>
            </div>
        </div>
    </div>
    <div class="container ">
        <div class="row">
            <div class="col-12" >
                <div class="text-container2 ">
                    <div>
                        <img class="hb2" src="../../photo/banner2.jpg"/>
                    </div>
                    <div>
                        <img class="icon-knife" src="../../photo/french-knife.png"/>
                    </div>
                    <div class="text-inner2 d-flex align-items-center">
                        餐盤貼近自己，<br/>
                        胸口倚靠桌面，
                        拿起漢堡/熱狗後，<br/>
                        施加點壓力擠壓，
                        大口咬下，<br/>
                        最後在雙唇離開食物前，<br/>
                        必須吸允湯(醬)汁，<br/>
                        我們擅長，
                        利用食材的細節堆疊，
                        創造出味蕾上的衝擊。
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.text-container{
    height: 300px;
    position: relative;
    margin-top: 150px;
}
.text-container2{
    height: 300px;
    position: relative;
}

.text-inner{
    position: relative; 
    z-index: 2; 
    border: 1px solid black ;
    height: 300px;
    margin-left: 200px;
    margin-right: 100px;
    padding: 70px 100px 70px 250px;
    background-color: #fff;
    font-size: 18px;
    font-family: 'font';
    line-height: 1.8;
}
.text-inner2{
    position: relative; 
    z-index: 2; 
    border: 1px solid black ;
    height: 300px;
    margin-left: 100px;
    margin-right: 200px;
    padding: 70px 250px 70px 100px;
    background-color: #fff;
    font-size: 18px;
    font-family: 'font';
    line-height: 1.8;
}

.hb{
    width: 300px;
    height: 300px;
    position: absolute; 
    top: -75px; 
    left: 75px; 
    z-index: 1000;
    border-radius: 50%;
    border:  1px solid black;
    transition: transform 0.3s ease;
}
.icon-fork{
    width: 200px;
    height: 200px;
    position: absolute; 
    top: 140px; 
    right: 50px; 
    z-index: 1000;
    animation: swing 1s infinite alternate;
}
.icon-knife{
    width: 200px;
    height: 200px;
    position: absolute; 
    top: 150px; 
    left: 30px; 
    z-index: 1000;
    animation: swing2 1s infinite alternate;
}
@keyframes swing {
    0% {
        transform:  rotate(5deg); /* 初始位置 */
    }
    100% {
        transform: rotate(-5deg); /* 回到初始位置并旋转-10度 */
    }
}
@keyframes swing2 {
    0% {
        transform: scaleX(-1) rotate(-5deg); /* 保持翻转并旋转 */
    }
    100% {
        transform: scaleX(-1) rotate(5deg); /* 回到初始位置 */
    }
}
.hb:hover{
    transform: scale(1.1);
}
.icon-bg{
    width: 2000px;
    height: 900px;
    position: absolute; 
    right: 0px; 
    top:-100px;
    left: 50%; /* 向左偏移50% */
    transform: translateX(-50%); /* 再向左偏移自身宽度的一半 */
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),url('../../photo/—Pngtree—close up of striped timber_15272361.jpg'); /* 原图片 */
    z-index: 0;
}

.hb2{
    width: 300px;
    height: 300px;
    position: absolute; 
    bottom: -75px; 
    right: 75px; 
    z-index: 1000;
    border-radius: 50%;
    border:  1px solid black;
    transition: transform 0.3s ease;
}
.hb2:hover{
    transform: scale(1.1);
}
.carousel-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 30px;
}
.carousel-item {
    height: 730px;
}
.carousel-inner {
    width: 100%;
    height: 100%;
    border-radius: 30px;
    overflow: hidden; /* 確保內容保持在圓角內 */
}
.card {
    z-index: 1000;
    height: 730px;
    padding: 0;
    border-radius: 30px;
    border: none;
    background-color: rgb(215, 215, 215);
    box-shadow: 5px 5px 16px rgb(90, 88, 88);
    transition: box-shadow 1s ease, border 1s ease; /* 添加過渡效果 */
}
.container {
    margin-top: 100px;
}
.bc2 {
    transition: background-color 1s ease; /* 添加過渡效果 */
    cursor: pointer;
}
.transparent {
    background-color: transparent; /* 背景變透明 */
    box-shadow: none; /* 隱藏陰影 */
    border: none; /* 隱藏邊框 */
}
.title {
    font-family: 'font';
    font-size: 36px;
    color: rgb(38, 31, 31);
    margin-top: 20px;
    margin-bottom: 20px;
}
.subtitle {
    font-family: 'font';
    font-size: 16px;
    letter-spacing: 0.1em;
    line-height: 2;
}
.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 1s ease-in-out;
    transform-style: preserve-3d;
    border-radius: 30px;
    background-color: rgb(10, 108, 87);
}
.inner-content {
    position: absolute;
    top: 15px; /* 內縮的距離 */
    left: 15px; /* 內縮的距離 */
    right: 15px; /* 內縮的距離 */
    bottom: 15px; /* 內縮的距離 */
    outline: 5px solid rgb(255, 255, 255); /* 內部邊框 */
    border-radius: 23px; /* 與外部圓角匹配 */
    transition: transform 1s ease-in-out;
    transform-style: preserve-3d;
}
.flip-card-inner:hover{
    background-color: rgb(10, 95, 77);
}
.flipped {
    transform: rotateY(180deg);
}
.flip-card-front,
.flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 30px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    color: #fff;
    background-color: rgb(10, 108, 87); /* 確保卡片不透明 */

}
.flip-card-inner:hover .flip-card-front,
.flip-card-inner:hover .flip-card-back {
    background-color: rgb(10, 95, 77); /* 前面和背面的背景顏色 */
}
.flip-card-back {
    transform: rotateY(180deg);
}
.carousel-control-prev,
.carousel-control-next {
    opacity: 0; /* 初始隱藏按鈕 */
    transition: opacity 0.3s ease; /* 淡入淡出的過渡效果 */
}
#carouselExampleControls:hover .carousel-control-prev,
#carouselExampleControls:hover .carousel-control-next {
    opacity: 1; /* 懸停時顯示按鈕 */
}
.fade-in {
    animation: fade-in 1.5s ease-in-out forwards;
}
@keyframes fade-in {
    from {
        opacity: 0;
        transform: translateX(-100px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
@media (max-width: 1200px) {
    .subtitle{
        font-size: 14px;
    }
    .carousel-item {
        height: 680px;
    }
    .card {
        height: 680px;
    }
    .icon-fork{
        width: 150px;
        height: 150px;
        top: 180px; 
    }
    .icon-knife{
        width: 150px;
        height: 150px;
        top: 190px; 
    }
    .text-inner{
        line-height: 1.5;
        font-size: 16px;
        padding: 70px 100px 70px 200px;
    }
    .text-inner2{
        line-height: 1.5;
        font-size: 16px;
    }
    .hb2{
        width: 250px;
        height: 250px;
    }
    .hb{
        width: 250px;
        height: 250px;
    }
}
@media (max-width: 992px) {
    .icon-fork{
        display: none;
    }
    .icon-knife{
        display: none;
    }
    .text-inner{
        line-height: 1.7;
        font-size: 14px;
        padding: 70px 50px 70px 200px;
        margin-left: 0px;
        margin-right: 0px;
    }
    .text-inner2{
        line-height: 1.7;
        font-size: 14px;
        padding: 70px 150px 70px 50px;
        margin-left: 0px;
        margin-right: 0px;
    }
    .hb{
        width: 200px;
        height: 200px;
        top: -75px; 
        left: -20px; 
    }
    .hb2{
        width: 200px;
        height: 200px;
        bottom: -75px; 
        right: -20px;
    }
}
@media (max-width: 576px) {
    .carousel-item {
        height: 530px;
    }
    .bc{
        height: 530px;
    }
    .flip-card-front,
    .flip-card-back {
        padding: 0px 15px;
    }
    .text-inner{
        line-height: 1.7;
        font-size: 14px;
        padding: 40px 20px 0px 20px;
        margin-left: 0px;
        margin-right: 0px;
    }
    .text-inner2{
        line-height: 1.7;
        font-size: 14px;
        padding: 0px 20px 40px 20px;
        margin-left: 0px;
        margin-right: 0px;
    }
    .hb{
        width: 150px;
        height: 150px;
        top: -75px; 
        left: 50%; 
        transform: translateX(-50%);
    }
    .hb2{
        width: 150px;
        height: 150px;
        bottom: -75px; 
        right: 50%;
        transform: translateX(50%);
    }
    .hb:hover{
        transform: translateX(-50%);
    }
    .hb2:hover{
        transform: translateX(  50%);
    }
}
</style>
