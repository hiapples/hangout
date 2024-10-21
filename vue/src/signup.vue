<script setup> 
    import { ref } from "vue";
    import { onMounted,onUpdated,onUnmounted } from "vue";
    import Nav_signup from "./components/signup/nav_signup.vue";
    import Banner_signup from "./components/signup/banner_signup.vue";

</script>
<template> 
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