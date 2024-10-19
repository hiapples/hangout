<script setup> 
    import { ref } from "vue";
    import { onMounted,onUpdated,onUnmounted } from "vue";
    import Nav from "./components/nav.vue";
    import Banner from "./components/banner.vue";
    import Back from "./components/back.vue";


</script>
<template>
    <div class="container-fluid" style="background-color: white;">
        <div class="row">
            <div class="col">
                <Nav ></Nav>
            </div>
        </div>
    </div>
    <Banner></Banner>
    <Back></Back>
    <br/><br/><br/><br/> <br/><br/><br/><br/> <br/><br/><br/><br/>
    <br/><br/><br/><br/> <br/><br/><br/><br/> <br/><br/><br/><br/>
    <br/><br/><br/><br/> <br/><br/><br/><br/> <br/><br/><br/><br/>
</template>

<style scoped>

 
</style>