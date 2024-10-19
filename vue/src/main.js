//載入createApp函式
import {createApp} from "vue";

//載入根組件
import App from "./app.vue";
import Signup from "./signup.vue";


//建立vue app物件
const app = createApp(App);
const signup = createApp(Signup);

//掛載到HTML標籤
app.mount("#app");
signup.mount("#signup");