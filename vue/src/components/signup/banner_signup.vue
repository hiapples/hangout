<script setup>
import { ref } from "vue";

// 定義變數來存儲用戶名、密碼、確認密碼和錯誤消息
const signupUserId = ref("");
const signupPassword = ref("");
const signupPassword2 = ref("");
const errorMessage = ref(""); // 用來顯示來自後端的錯誤消息
const successMessage = ref(""); // 顯示成功消息

function submitSignup() {
    // 檢查用戶名是否為空
        if (!signupUserId.value.trim()) {
        errorMessage.value = "Username cannot be empty";
        triggerAlertAnimation();
        return; // 錯誤後面不執行
    }
    // 檢查用戶名長度
    if (signupUserId.value.length < 3 || signupUserId.value.length > 15) {
        errorMessage.value = "Username must be between 3 and 15 characters";
        triggerAlertAnimation();
        return; // 錯誤後面不執行
    }

    // 檢查密碼是否為空
    if (!signupPassword.value.trim()) {
        errorMessage.value = "Password cannot be empty";
        triggerAlertAnimation();
        return; // 錯誤後面不執行
    }
    // 檢查密碼長度
    if (signupPassword.value.length < 6) {
        errorMessage.value = "Password must be at least 6 characters long";
        triggerAlertAnimation();
        return; // 錯誤後面不執行
    }
    // 檢查確認密碼是否為空
    if (!signupPassword2.value.trim()) {
        errorMessage.value = "Please confirm your password";
        triggerAlertAnimation();
        return; // 錯誤後面不執行
    }

    // 檢查密碼是否一致
    if (signupPassword.value !== signupPassword2.value) {
        errorMessage.value = "Two passwords are inconsistent";
        triggerAlertAnimation();
        return; // 錯誤後面不執行
    }

    const formData = new FormData();
    formData.append('signup_userid', signupUserId.value);
    formData.append('signup_password', signupPassword.value);

    fetch('/signuping', { method: 'POST', body: formData })
        .then(response => response.json())
        .then(responseData => {
            if (responseData.success) {
                successMessage.value = responseData.message;
                errorMessage.value = ""; // 清除錯誤消息
                document.querySelector(".button").disabled = true;
                setTimeout(() => {  
                    window.location.href = '/signin';
                }, 2000); // 2秒後重定向
            } else {
                errorMessage.value = responseData.message;
                successMessage.value = ""; // 清除成功消息
                triggerAlertAnimation(); // 觸發錯誤消息動畫
            }
        })
        .catch(error => {
            console.error('Error:', error);
            errorMessage.value = 'An error occurred during submission';
            successMessage.value = ""; // 清除成功消息
            triggerAlertAnimation(); // 觸發錯誤消息動畫
        });
}


function triggerAlertAnimation() {
    const alertBox = document.querySelector(".alert");
    if (alertBox) {
        alertBox.classList.remove('scale-reset'); // 移除重置類
        alertBox.offsetWidth; // 觸發重排來讓動畫生效
        alertBox.classList.add('scale-active'); // 添加放大的類名

        // 1秒後移除放大的類名，恢復原狀
        setTimeout(() => {
            alertBox.classList.remove('scale-active'); // 移除放大效果
            alertBox.classList.add('scale-reset'); // 恢復到原始大小
        }, 200); 
    }
}

</script>

<template>
    <div class="body">
        <div class="wrapper">
            <h1>Register</h1>
            <form @submit.prevent="submitSignup">
                <div class="input-box">
                    <input v-model="signupUserId" type="text" placeholder="Username" autocomplete="off" />
                    <i class="bx bxs-user"></i>
                </div>
                <div class="input-box">
                    <input v-model="signupPassword" type="password" placeholder="Password" />
                    <i class="bx bxs-lock-alt"></i>
                </div>
                <div class="input-box">
                    <input v-model="signupPassword2" type="password" placeholder="Confirm Password" />
                    <i class="bx bxs-lock-alt"></i>
                </div>
                <button class="button btn btn-primary">Sign up</button>
                <div class="register-link">
                    <p>Do you have an account?&ensp;<router-link to="/signin">Login</router-link></p>
                </div>
                <div class="mt-3">
                    <div v-if="errorMessage" class="alert alert-danger" ref="alertBox">{{ errorMessage }}</div>
                    <div v-if="successMessage" class="alert alert-success" ref="alertBox">{{ successMessage }}</div>
                </div>
            </form>
        </div>
    </div>
</template>

<style scoped>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Poppins', sans-serif;
    }
    .body {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background: url("../../photo/244253280_241288671346732_2915103136200946263_n.jpg") no-repeat;
        background-size: cover;
        background-position: bottom;
    }
    .wrapper {
        width: 420px;
        background: transparent;
        border: 2px solid rgba(255, 255, 255, .2);
        backdrop-filter: blur(35px);
        box-shadow: 0 0 10px rgba(0, 0, 0, .2);
        color: #fff;
        border-radius: 10px;
        padding: 30px 40px;
    }
    .wrapper h1 {
        font-size: 36px;
        text-align: center;
    }
    .wrapper .input-box {
        width: 100%;
        height: 50px;
        margin: 30px 0;
    }
    .input-box input {
        width: 100%;
        height: 100%;
        background: transparent;
        border: none;
        outline: none;
        border: 2px solid rgba(255, 255, 255, .2);
        border-radius: 40px;
        font-size: 16px;
        color: #fff;
        padding: 20px 45px 20px 20px;
    }
    .input-box input::placeholder {
        color: #9c9696;
    }
    .input-box {
        position: relative;
    }
    .input-box i {
        position: absolute;
        right: 20px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 20px;
    }
    .wrapper .button {
        width: 100%;
        height: 45px;
        background: #fff;
        border: none;
        outline: none;
        border-radius: 40px;
        box-shadow: 0 0 10px rgba(0, 0, 0, .1);
        cursor: pointer;
        font-size: 16px;
        color: #333;
        font-weight: 600;
    }
    .wrapper .register-link {
        font-size: 14.5px;
        text-align: center;
        margin: 20px 0 15px;
    }
    .register-link p a {
        color: #fff;
        text-decoration: none;
        font-weight: 600;
    }
    .register-link p a:hover {
        text-decoration: underline;
    }
    .alert {
        padding: 10px;
        transition: transform 0.3s ease;
        text-align: center;
    }

    .scale-active {
        transform: scale(1.1); /* 放大1.2倍 */
        transition: transform 0.2s ease; /* 設置放大1秒 */
    }

    .scale-reset {
        transform: scale(1); /* 恢復原始大小 */
        transition: transform 0.3s ease; /* 回縮的過渡效果 */
    }

    @media (max-width: 576px) {
        .wrapper {
            width: 380px;
        }
    }
</style>
