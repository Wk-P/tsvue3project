<template>
    <ul class="order-block">
        <li v-for="(o, i) in ordersList" :key="i">
            {{ o }}
        </li>
    </ul>
</template>

<script setup lang="ts" name="orders">
import { ref } from 'vue';
const ordersList = ref(["o1", "o2", "o3", "o4", "o5"]);

</script>
<style scoped>

.order-block {
    list-style: none;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 20px;
}

.order-block li {
    border: 3px solid #999;
    height: 100px;
}
</style>
