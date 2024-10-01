<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const isSmallScreen = ref(false);

const checkScreenSize = () => {
  isSmallScreen.value = window.innerWidth < 768;
};

// Function to replace slashes with <wbr> in English descriptions
const replaceSlashes = () => {
  const elements = document.querySelectorAll('.en');
  elements.forEach(function(element) {
    element.innerHTML = element.innerHTML.replace(/\//g, '/<wbr>');
  });
};

onMounted(() => {
  checkScreenSize();
  window.addEventListener("resize", checkScreenSize);
  replaceSlashes(); // Call the function after the component mounts
});

onUnmounted(() => {
  window.removeEventListener("resize", checkScreenSize);
});
</script>

<template>
  <div class="menu-container mt-3">
    <div class="logo-container">
      <div class="menu mt-3 mb-2">MENU</div>
    </div>
    <div class="container-fluid">
      <div class="row g-2">
        <!-- First Column -->
        <div class="col-6 col-md-4">
          <div class="title">BURGERS (BEEF/PORK)</div>
          <div class="subtitle">
            <ol>
              <li class="mt-2">
                <div>美國夢幻起司<span class="red">150$</span></div>
                <div class="en">FriedCheese/Pickles</div>
              </li>
              <li class="mt-2">
                <div>藍調爵士起司<span class="red">170$</span></div>
                <div class="en">FriedBlueCheese/Pickles</div>
              </li>
              <li class="mt-2">
                <div>夏威夷燒烤醬<span class="red ">170$</span></div>
                <div class="en">Pineapple/HandMade BBQSauce</div>
              </li>
              <li class="mt-2">
                <div>皇后區焦糖<span class="red ">180$</span></div>
                <div class="en">HandMade Salted Caramel Sauce/DriedStrawBerry/DriedOrangeSlices</div>
              </li>
              <li class="mt-2">
                <div>香草松露野菇<span class="red ">190$</span></div>
                <div class="en">Mushroom/TruffleSauce</div>
              </li>
              <li class="mt-2">
                <div>南方炸雞三明治<span class="red ">200$</span></div>
                <div class="en">SouthernFriedChicken/Pickles/HomemadeToast/Onion/Fries</div>
              </li>
              <li class="mt-2">
                <div>辣刀堡<span class="red ">200$</span></div>
                <div class="en">HotMeatSauce/SourCream/CheeseChiliRoll</div>
              </li>
              <li class="mt-2">
                <div>天使醬通心粉<span class="red ">200$</span></div>
                <div class="en">Bacon/Mac&Cheese/CheeseSauce</div>
              </li>
              <li class="mt-2">
                <div>墨西哥酪梨<span class="red ">250$</span></div>
                <div class="en">AvocadoSlices/Salsa/Pesto/jalapeno/SourCream</div>
              </li>
              <li class="mt-2">
                <div>德州主烤官<span class="red ">270$</span></div>
                <div class="en">16hrSmokedBrisket/BeefPatty/Pickles/4hrSmokedWhiskyBBQSauce</div>
              </li>
            </ol>
          </div>
        </div>

        <!-- Second Column -->
        <div class="col-6 col-md-4">
          <div class="title">HOT DOGS (PORK)</div>
          <div class="subtitle">
            <ol>
              <li class="mt-2">
                <div>德式脆腸豬肉堡<span class="red">100$</span></div>
                <div class="en">ClassicBacon</div>
              </li>
              <li class="mt-2">
                <div>北美燉肉香辣脆腸堡<span class="red">110$</span></div>
                <div class="en">HotMeatSauce</div>
              </li>
              <li class="mt-2">
                <div>酸豆手撕豬肉脆腸堡<span class="red">120$</span></div>
                <div class="en">PulledPork</div>
              </li>
              <li class="mt-2">
                <div>狼煙牛胸肉脆腸堡<span class="red">170$</span></div>
                <div class="en">16hrSmokedBrisket</div>
              </li>
            </ol>
          </div>
          <div class="title mt-5">SIDES</div>
          <div class="subtitle">
            <ol>
              <li class="mt-2">
                <div>薯條<span class="red">60$</span></div>
                <div class="en">French Fries</div>
              </li>
              <li class="mt-2">
                <div>起司薯條<span class="red ">80$</span></div>
                <div class="en">Cheese Fries</div>
              </li>
              <li class="mt-2">
                <div>洋蔥圈<span class="red ">70$</span></div>
                <div class="en">Onion Rings</div>
              </li>
              <li class="mt-2">
                <div>洋蔥圈<span class="red ">70$</span></div>
                <div class="en">Onion Rings</div>
              </li>
            </ol>
          </div>

          <!-- Display dining instructions if on small screen -->
          <div v-if="isSmallScreen">
            <div class="title mt-5">用餐須知</div>
            <div class="subtitle" style="white-space:wrap;">
              <ul>
                <li class="mt-2">
                  <div>餐點皆現做，請給予多一點耐心。</div>
                </li>
                <li class="mt-2">
                  <div>請於櫃檯點餐及結帳。</div>
                </li>
                <li class="mt-2">
                  <div>禁帶外食，理性溝通。</div>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Third Column -->
        <div class="col-6 col-md-4 three">
          <div class="title">DRINKS</div>
          <div class="subtitle">
            <ol>
              <li class="mt-2">
                <div>可樂<span class="red ">50$</span></div>
                <div class="en">Coke</div>
              </li>
              <li class="mt-2">
                <div>雪碧<span class="red ">50$</span></div>
                <div class="en">Sprite</div>
              </li>
              <li class="mt-2">
                <div>冰紅茶<span class="red">50$</span></div>
                <div class="en">Iced Tea</div>
              </li>
            </ol>
          </div>

          <!-- Display dining instructions if on larger screens -->
          <div v-if="!isSmallScreen">
            <div class="title mt-5">用餐須知</div>
            <div class="subtitle" style="white-space:wrap;">
              <ul>
                <li class="mt-2">
                  <div>餐點皆現做，請給予多一點耐心。</div>
                </li>
                <li class="mt-2">
                  <div>請於櫃檯點餐及結帳。</div>
                </li>
                <li class="mt-2">
                  <div>禁帶外食，理性溝通。</div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.menu-container {
  overflow-y: hidden;
}
.title {
  font-size: 30px;
  font-family: 'font';
  font-weight: bold;
  margin-left: 80px;
}
.subtitle {
  font-size: 22px;
  font-family: 'font';
  margin-left: 80px;
  white-space: nowrap;
  font-weight: bold;
}
.red {
  font-size: 22px;
  font-family: 'font';
  color: rgb(113, 14, 14);
  white-space: nowrap;


}
.en {
  font-size: 18px;
  font-family: 'font';
  white-space: normal; 
  overflow-wrap: break-word;
  font-weight: normal;
}
.menu-container {
  background: linear-gradient(to bottom, rgba(255, 255, 255, 0.096) 70%, rgba(255, 255, 255, 0.228) 85%, rgba(255, 255, 255, 0.196) 100%), 
              url('/src/photo/—Pngtree—rough kraft paper background_1232396.jpg') no-repeat left center;
  background-size: cover;
  height: 950px;
}



.logo {
  width: 300px;
  border-radius: 20px;
  box-shadow: 5px 5px 8px black;
}
.logo-container {
  display: flex;
  justify-content: center;
  margin-bottom: 50px;
}
.menu {
  font-size: 40px;
  font-family: 'font';
  border-top: 3px solid #000;
  border-bottom: 3px solid #000;
}
@media (max-width: 1200px) {
  .title {
    font-size: 25px;
    margin-left: 50px;
  }
  .subtitle {
    font-size: 20px;
    margin-left: 50px;
  }
  .red {
    font-size: 20px;
  }
  .en {
    font-size: 20px;
  }
}
@media (max-width: 992px) {
  .title {
    font-size: 22px;
    margin-left: 30px;
  }
  .subtitle {
    font-size: 18px;
    margin-left: 30px;
  }
  .red {
    font-size: 18px;
  }
  .en {
    font-size: 18px;
  }
  li {
    margin-bottom: 15px;
  }
}
@media (max-width: 768px) {
  .menu-container {
    height: 1200px;
  }
  .three{
    margin-top: -120px;
  }
}
@media (max-width: 576px) {
  .menu-container {
    height: 1200px;
  }
  .three{
    margin-top: 30px;
  }
  .title {
    font-size: 16px;
    margin-left: 0px;
  }
  .subtitle {
    font-size: 14px;
    margin-left: -10px;
  }
  .red {
    font-size: 14px;
  }
  .en {
    font-size: 12px;
  }
}
</style>
