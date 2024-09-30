<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const isSmallScreen = ref(false);

const checkScreenSize = () => {
  isSmallScreen.value = window.innerWidth < 768;
};

onMounted(() => {
  checkScreenSize();
  window.addEventListener("resize", checkScreenSize);
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
      <div class="row">
        <!-- 第一欄 -->
        <div class="col-6 col-md-4">
          <div class="title">BURGERS (BEEF/PORK)</div>
          <div class="subtitle">
            <ol>
              <li class="mt-2">
                <div>美國夢幻起司<span class="red ms-3">150$</span></div>
                <div class="en">Fried Cheese/Pickles</div>
              </li>
              <li class="mt-2">
                <div>墨西哥辣味牛肉<span class="red ms-3">160$</span></div>
                <div class="en">Spicy Beef/Jalapenos</div>
              </li>
              <li class="mt-2">
                <div>香脆雞肉堡<span class="red ms-3">170$</span></div>
                <div class="en">Crispy Chicken/Lettuce</div>
              </li>
              <li class="mt-2">
                <div>美式經典牛肉<span class="red ms-3">180$</span></div>
                <div class="en">Classic Beef/Cheddar</div>
              </li>
              <li class="mt-2">
                <div>美式經典牛肉<span class="red ms-3">180$</span></div>
                <div class="en">Classic Beef/Cheddar</div>
              </li>
              <li class="mt-2">
                <div>美式經典牛肉<span class="red ms-3">180$</span></div>
                <div class="en">Classic Beef/Cheddar</div>
              </li>
              <li class="mt-2">
                <div>美式經典牛肉<span class="red ms-3">180$</span></div>
                <div class="en">Classic Beef/Cheddar</div>
              </li>
              <li class="mt-2">
                <div>美式經典牛肉<span class="red ms-3">180$</span></div>
                <div class="en">Classic Beef/Cheddar</div>
              </li>
              <li class="mt-2">
                <div>美式經典牛肉<span class="red ms-3">180$</span></div>
                <div class="en">Classic Beef/Cheddar</div>
              </li>
              <li class="mt-2">
                <div>美式經典牛肉<span class="red ms-3">180$</span></div>
                <div class="en">Classic Beef/Cheddar</div>
              </li>
            </ol>
          </div>
        </div>

        <!-- 第二欄 -->
        <div class="col-6 col-md-4">
          <div class="title">HOT DOGS (PORK)</div>
          <div class="subtitle">
            <ol>
              <li class="mt-2">
                <div>美國經典熱狗<span class="red ms-3">120$</span></div>
                <div class="en">Classic Dog/Mustard</div>
              </li>
              <li class="mt-2">
                <div>起司熱狗<span class="red ms-3">130$</span></div>
                <div class="en">Cheese Dog/Onions</div>
              </li>
              <li class="mt-2">
                <div>辣味熱狗<span class="red ms-3">140$</span></div>
                <div class="en">Spicy Dog/Chili</div>
              </li>
              <li class="mt-2">
                <div>辣味熱狗<span class="red ms-3">140$</span></div>
                <div class="en">Spicy Dog/Chili</div>
              </li>
            </ol>
          </div>
          <div class="title mt-5">SIDES</div>
          <div class="subtitle">
            <ol>
              <li class="mt-2">
                <div>薯條<span class="red ms-3">60$</span></div>
                <div class="en">French Fries</div>
              </li>
              <li class="mt-2">
                <div>起司薯條<span class="red ms-3">80$</span></div>
                <div class="en">Cheese Fries</div>
              </li>
              <li class="mt-2">
                <div>洋蔥圈<span class="red ms-3">70$</span></div>
                <div class="en">Onion Rings</div>
              </li>
              <li class="mt-2">
                <div>洋蔥圈<span class="red ms-3">70$</span></div>
                <div class="en">Onion Rings</div>
              </li>
            </ol>
          </div>

          <!-- 如果是小螢幕，將用餐須知顯示在這裡 -->
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

        <!-- 第三欄 -->
        <div class="col-6 col-md-4 three">
          <div class="title">DRINKS</div>
          <div class="subtitle">
            <ol>
              <li class="mt-2">
                <div>可樂<span class="red ms-3">50$</span></div>
                <div class="en">Coke</div>
              </li>
              <li class="mt-2">
                <div>雪碧<span class="red ms-3">50$</span></div>
                <div class="en">Sprite</div>
              </li>
              <li class="mt-2">
                <div>冰紅茶<span class="red ms-3">50$</span></div>
                <div class="en">Iced Tea</div>
              </li>
            </ol>
          </div>

          <!-- 如果不是小螢幕，將用餐須知顯示在這裡 -->
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
  white-space: nowrap;
}
.menu-container {
  background: linear-gradient(to bottom, rgba(255, 255, 255, 0.096) 70%, rgba(255, 255, 255, 0.2) 85%, rgba(255, 255, 255, 0.196) 100%), 
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
        height: 1050px;
    }
  .three{
    margin-top: -120px;
  }
  .title {
    font-size: 16px;
    margin-left: 5px;
  }
  .subtitle {
    font-size: 14px;
    margin-left: 5px;
  }
  .red {
    font-size: 14px;
  }
  .en {
    font-size: 14px;
  }

}
</style>
