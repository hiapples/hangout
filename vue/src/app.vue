<script setup> 
    import { ref } from "vue";
    import { onMounted,onUpdated,onUnmounted } from "vue";

</script>
<template>
    <router-view></router-view>
</template>

<style scoped>
@font-face {
  font-family: 'font';
  src: url('/src/fonts/font.otf') format('opentype');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'font3';
  src: url('/src/fonts/font3.ttf') format('opentype');
  font-weight:normal;
  font-style: normal;
}
</style>