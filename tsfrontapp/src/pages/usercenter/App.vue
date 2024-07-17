<template>
    <HeadNav/>
    <div class="blocks">
        <div class="head-outer">
            <img src="" alt="avator" />
            <ul>
                <li><RouterLink :to="{ name : 'orders' }" class="inner-block">订单</RouterLink></li>
                <li><RouterLink :to="{ name : 'cart' }" class="inner-block">购物车</RouterLink></li>
                <li><RouterLink :to="{ name : 'favorite' }" class="inner-block">收藏</RouterLink></li>
            </ul>
        </div>
        <div class="top-line"></div>
        <div class="container-block">
            <RouterView></RouterView>
        </div>
    </div>
</template>

<script lang="ts" setup name="usercenter">
import HeadNav from "@/components/HeadNav.vue";
import { RouterLink, RouterView } from "vue-router";
</script>
<style scoped>
.blocks {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    width: 100%;
    box-sizing: border-box;
}

.head-outer {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    height: 80px;
    box-sizing: border-box;
}

.head-outer img {
    border: 4px solid brown;
    height: 100%;
    aspect-ratio: 1;
    box-sizing: border-box;
}

.head-outer ul {
    display: flex;
    flex-direction: row;
    justify-content: end;
    list-style: none;
    box-sizing: border-box;
    background-color: rgba(244, 244, 244, 0.5);
}

.head-outer ul li {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    padding: 0 20px;
    box-sizing: border-box;
}

.head-outer ul li:hover {
    cursor: pointer;
    background-color: rgba(235, 235, 235, 1);
}


.container-block {
    width: calc(100% - 100px);
    height: 100%;
    border: 4px solid brown;
    box-sizing: border-box;
    margin: 50px;
    padding: 30px;
}

.top-line {
    display: flex;
    height: 5px;
    width: 100%;
    background: linear-gradient(
        to right,
        rgb(190, 226, 240),
        #fff,
        rgb(190, 226, 240)
    );
}

.inner-block {
    box-sizing: border-box;
    width: 100%;
    background-color: rgba(243, 243, 243, 0.5);
    border: solid #fff 5px;
    border-radius: 5px;
    margin: 20px 0;
}

.inner-block h3 {
    padding: 30px 0;
    text-align: center;
    background-color: rgba(243, 243, 243, 0.5);
}

.inner-block ul {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    list-style: none;
    width: 100%;
    padding: 20px 0;
}

.inner-block ul li {
    width: auto;
    height: 200px;
    background-color: rgba(243, 243, 243, 0.5);
    margin: 0 20px;
}
</style>
