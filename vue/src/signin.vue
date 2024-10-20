<script setup> 
    import { ref } from "vue";
    import { onMounted,onUpdated,onUnmounted } from "vue";
    import Nav_signin from "./components/nav_signin.vue";
    import Banner_signin from "./components/banner_signin.vue";

</script>
<template> 
    <Banner_signin></Banner_signin>
    <div class="container-fluid" style="background-color: white;">
        <div class="row">
            <div class="col">
                <Nav_signin></Nav_signin>
            </div>
        </div>
    </div>
</template>

<style scoped>

 
</style>