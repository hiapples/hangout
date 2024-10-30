<script setup> 
    import { ref } from "vue";
    import { onMounted,onUpdated,onUnmounted } from "vue";
    import Nav from "./components/index/nav.vue";
    import Banner from "./components/index/banner.vue";
    import Back from "./components/index/back.vue";
    import About from "./components/index/about.vue";
    import News from "./components/index/news.vue";
    import Menu from "./components/index/menu.vue";
    import Opening from "./components/index/opening.vue";
    import Nav_signin from "./components/signin/nav_signin.vue";
    import Banner_signin from "./components/signin/banner_signin.vue";
    import Nav_signup from "./components/signup/nav_signup.vue";
    import Banner_signup from "./components/signup/banner_signup.vue";
</script>
<template>
    <Opening></Opening>
    <div class="container-fluid">
        <div class="row">
            <div class="col">
                <Nav ></Nav>
            </div>
        </div>
    </div>
    <Banner></Banner>
    <About></About>
    <News></News>
    <Menu></Menu>
    <Back></Back>
    <br/><br/><br/><br/> <br/><br/><br/><br/> <br/><br/><br/><br/>
    <Banner_signin></Banner_signin>
    <div class="container-fluid" style="background-color: white;">
        <div class="row">
            <div class="col">
                <Nav_signin></Nav_signin>
            </div>
        </div>
    </div>
    <br/><br/><br/><br/> <br/><br/><br/><br/> <br/><br/><br/><br/>
    <Banner_signup></Banner_signup>
    <div class="container-fluid" style="background-color: white;">
        <div class="row">
            <div class="col">
                <Nav_signup></Nav_signup>
            </div>
        </div>
    </div>
</template>

<style scoped>

 
</style>