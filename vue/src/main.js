//載入createApp函式
import {createApp} from "vue";

//載入根組件
import App from "./app.vue";
import Signup from "./signup.vue";
import Signin from "./signin.vue";


//建立vue app物件
const app = createApp(App);
const signup = createApp(Signup);
const signin = createApp(Signin);

//掛載到HTML標籤
app.mount("#app");
signup.mount("#signup");
signin.mount("#signin");