//載入createApp函式
import {createApp} from "vue";

//載入根組件
import App from "./app.vue";
//import router from './router/router.js'; 


//建立vue app物件
const app = createApp(App);

//app.use(router); // 使用 router

//掛載到HTML標籤
app.mount("#app");
