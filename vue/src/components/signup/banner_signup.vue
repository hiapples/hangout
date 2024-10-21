<script setup>
import { ref } from "vue";
import { onMounted, onUpdated, onUnmounted } from "vue";


</script>

<template>
    <div class="body">
        <div class="wrapper">
            <form action="/signuping" method="post">
                <h1>Register</h1>
                <div class="input-box"> 
                    <input id="signup_userid" name="signup_userid" type="text" placeholder="Username" required/>
                    <i class='bx bxs-user'></i>
                </div>
                <div class="input-box"> 
                    <input id="signup_password" name="signup_password" type="password" placeholder="Password" required/>
                    <i class='bx bxs-lock-alt'></i>
                </div>
                <div class="input-box"> 
                    <input id="signup_password2" name="signup_password2" type="password" placeholder="ConfirmPassword" required/>
                    <i class='bx bxs-lock-alt'></i>
                </div>
                <button class="btn" >Signup</button>
                <div class="register-link">
                    <p>Do you have an account?&ensp;<a href="/signin">Login</a></p>
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
    font-family: 'Poppins',sans-serif   ;
}
.body{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: url("../../photo/244253280_241288671346732_2915103136200946263_n.jpg") no-repeat;
    background-size: cover;
    background-position:bottom;
}
.wrapper{
    width: 420px;
    background:transparent;
    border:2px solid rgba(255,255,255,.2);
    backdrop-filter: blur(35px);
    box-shadow: 0 0 10px rgba(0,0,0,.2);
    color: #fff;
    border-radius: 10px;
    padding: 30px 40px;
}
.wrapper h1{
    font-size: 36px;
    text-align: center;
}
.wrapper .input-box{
    width: 100%;
    height: 50px;
    margin: 30px 0;
}
.input-box input{
    width: 100%;
    height: 100%;
    background: transparent;
    border: none;
    outline: none;
    border:2px solid rgba(255,255,255,.2);
    border-radius: 40px;
    font-size: 16px;
    color: #fff;
    padding: 20px 45px 20px 20px ;
}
.input-box input::placeholder{
    color: #9c9696;
}
.input-box{
    position:relative
}
.input-box i{
    position: absolute;
    right:20px;
    top:50%;
    transform: translateY(-50%);
    font-size: 20px;
}


.wrapper .btn{
    width: 100%;
    height: 45px;
    background: #fff;
    border: none;
    outline: none;
    border-radius: 40px;
    box-shadow: 0 0 10px rgba(0,0,0,.1);
    cursor: pointer;
    font-size: 16px;
    color: #333;
    font-weight: 600;
}
.wrapper .register-link{
    font-size: 14.5px;
    text-align:center;
    margin: 20px 0 15px;
}
.register-link p a{
    color: #fff;
    text-decoration: none;
    font-weight: 600;
}
.register-link p a:hover{
    text-decoration: underline;
}
@media (max-width: 576px) {
    .wrapper{
        width: 380px;
    }
}
</style>
