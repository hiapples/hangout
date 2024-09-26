<script setup> 
    import { ref } from "vue";
    import { onMounted,onUpdated,onUnmounted } from "vue";
    import Nav from "./nav.vue";
    import Banner from "./banner.vue";
    import Opening from "./opening.vue";
    import Back from "./back.vue";
    import About from "./about.vue";
    import News from "./news.vue";
    import Menu from "./menu.vue";

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
    <Back></Back>
    <br/><br/><br/><br/> <br/><br/><br/><br/> <br/><br/><br/><br/>
</template>

<style scoped>

 
</style>