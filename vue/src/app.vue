<script setup> 
    import { ref } from "vue";
    import { onMounted,onUpdated,onUnmounted } from "vue";
    import Opening from "./components/index/opening.vue";
</script>
<template>
    <Opening></Opening>
    <router-view></router-view>
</template>

<style scoped>

</style>