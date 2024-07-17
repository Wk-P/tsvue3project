<template>
    <RouterView></RouterView>
    <FooterLine />
</template>

<script lang="ts" setup>
import FooterLine from "./components/FooterLine.vue";
import { RouterView } from "vue-router";
</script>

<style scoped>
</style>
