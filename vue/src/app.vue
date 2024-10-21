<script setup> 
    import { ref } from "vue";
    import { onMounted,onUpdated,onUnmounted } from "vue";
    import Nav from "./components/nav.vue";
    import Banner from "./components/banner.vue";
    import Opening from "./components/opening.vue";
    import Back from "./components/back.vue";
    import About from "./components/about.vue";
    import News from "./components/news.vue";
    import Menu from "./components/menu.vue";

    import Signin from "./signin.vue";
    import Signup from "./signup.vue";

</script>
<template>
    <Opening></Opening>
    <div class="container-fluid" style="background-color: white;">
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
</template>

<style scoped>

 
</style>