<script setup>
import { ref } from "vue";

// 定義變數來存儲用戶名、密碼、確認密碼和錯誤消息
const signupUserId = ref("");
const signupPassword = ref("");
const signupPassword2 = ref("");
const errorMessage = ref(""); // 用來顯示來自後端的錯誤消息
const successMessage = ref(""); // 顯示成功消息

// 提交表單處理函數
function submitSignup() {
    // 檢查密碼是否一致
    if (signupPassword.value !== signupPassword2.value) {
        errorMessage.value = "兩次密碼不一致";
        return;
    }

    const formData = new FormData();
    formData.append('signup_userid', signupUserId.value);
    formData.append('signup_password', signupPassword.value);

    fetch('/signuping', {method: 'POST',body: formData})
    .then(response => response.json()) 
    .then(responseData => {
        if (responseData.success) {
            successMessage.value = responseData.message;
            errorMessage.value = ""; // 清除錯誤消息
            // 重定向到登入頁面
            setTimeout(() => {
                window.location.href = '/signin';
            }, 2000); // 2秒後重定向
        } else {
            errorMessage.value = responseData.message;
            successMessage.value = ""; // 清除成功消息
        }
    })
    .catch(error => {
        console.error('Error:', error);
        errorMessage.value = '提交過程中發生錯誤';
        successMessage.value = ""; // 清除成功消息
    });
}
</script>

<template>
    <div class="body">
        <div class="wrapper">
            <h1>Register</h1>
            <form @submit.prevent="submitSignup">
                <div class="input-box">
                    <input v-model="signupUserId" type="text" placeholder="Username" required/>
                    <i class="bx bxs-user"></i>
                </div>
                <div class="input-box">
                    <input v-model="signupPassword" type="password" placeholder="Password" required/>
                    <i class="bx bxs-lock-alt"></i>
                </div>
                <div class="input-box">
                    <input v-model="signupPassword2" type="password" placeholder="Confirm Password" required/>
                    <i class="bx bxs-lock-alt"></i>
                </div>
                <button class="button btn btn-primary">Signup</button>
                <div class="register-link">
                    <p>Do you have an account?&ensp;<router-link to="/signin">Login</router-link></p>
                    <div class="mt-3">
                        <div v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</div>
                        <div v-if="successMessage" class="alert alert-success">{{ successMessage }}</div>
                    </div>
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
    .alert{
        padding: 10px;
    }
    @media (max-width: 576px) {
        .wrapper {
            width: 380px;
        }
    }
</style>
