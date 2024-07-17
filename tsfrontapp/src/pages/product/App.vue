<template>
    <HeadNav />
    <div class="head-on">
        <RouterLink to="/">
            <img src="/arrow-left.png" alt="turn back" />
            <div>返回</div>
        </RouterLink>
    </div>
    <div class="outer">
        <div class="product-detail-block">
            <h2 class="title">{{ item?.name }}</h2>
            <div class="product-img">
                <img src="/lv.png" alt="item-img" />
            </div>
            <div class="details">
                <ul class="details-list">
                    <li>
                        <RouterLink :to="{ name: 'details' }" class="item-link"
                            >详情</RouterLink
                        >
                    </li>
                    <li>
                        <RouterLink :to="{ name: 'comments' }" class="item-link"
                            >评论</RouterLink
                        >
                    </li>
                </ul>
            </div>
            <RouterView></RouterView>
        </div>
    </div>
</template>

<script lang="ts" setup name="product">
import HeadNav from "@/components/HeadNav.vue";
import { useItemStore } from "@/stores";
import { ref, watch, onMounted, computed } from "vue";
import { RouterLink, RouterView, useRoute } from "vue-router";
const store = useItemStore();

// 动态计算 item 属性
const item = computed(() => store.item);

const currentComponent = ref("details");

// 获取路由信息
const route = useRoute();

// 监听路由变化
watch(
    () => route.name,
    (to) => {
        if (to) {
            currentComponent.value = to.toString(); // Ensure to convert to string
        }
    }
);
</script>

<style scoped>
.outer {
    height: auto;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding-top: 40px;
    padding-bottom: 40px;
}

.product-detail-block {
    width: 50%;
    border-radius: 4px;
    box-shadow: 0 0 10px 2px #eee;
    border: 3px solid rgb(255, 200, 0);
    display: flex;
    flex-direction: column;
    align-items: center;
}

.details {
    width: 100%;
}

.details-list {
    list-style: none;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
    width: 100%;
    height: 50px;
}

.details-list li {
    border-top: 2px solid rgb(255, 200, 0);
    text-align: center;
    background-color: rgba(255, 200, 0, 0.5);
    height: 100%;
    width: 100%;
}

.details-list li:hover {
    background-color: rgba(255, 200, 0, 1);
    cursor: pointer;
}

.item-link {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    text-decoration: none;
    color: black;
    box-sizing: border-box;
}

.title {
    padding: 20px 0;
}

.product-img {
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding: 10px 20px 40px 20px;
    width: 100%;
    height: 500px;
    box-sizing: border-box;
}

.product-img img {
    border: 4px solid rgba(255, 200, 0, 1);
    box-sizing: border-box;
    background-color: #eee;
    height: 100%;
}

.inner-details {
    box-sizing: border-box;
    width: 100%;
    border: 3px solid black;
    height: 200px;
}

.head-on {
    height: 50px;
    display: flex;
    flex-direction: row;
    align-items: center;
    background-color: rgb(244, 244, 244);
}

.head-on a {
    height: 100%;
    width: auto;
    display: flex;
    flex-direction: row;
    text-decoration: none;
    box-sizing: border-box;
    border: 2px solid rgb(244, 244, 244);
}

.head-on a div {
    height: 100%;
    width: auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    color: black;
    padding-right: 20px;
    padding-left: 5px;
}

.head-on img {
    box-sizing: border-box;
    height: 100%;
    width: auto;
}
.head-on a:hover {
    cursor: pointer;
    border: 2px solid #ccc;
}
</style>
