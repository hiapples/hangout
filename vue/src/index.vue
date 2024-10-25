<script setup> 
    import { ref } from "vue";
    import { onMounted,onUpdated,onUnmounted } from "vue";
    import Nav from "./components/index/nav.vue";
    import Banner from "./components/index/banner.vue";
    import Opening from "./components/index/opening.vue";
    import Back from "./components/index/back.vue";
    import About from "./components/index/about.vue";
    import News from "./components/index/news.vue";
    import Menu from "./components/index/menu.vue";

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
</template>

<style scoped>

 
</style>