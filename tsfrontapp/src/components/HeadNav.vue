<template>
    <nav class="head-nav">
        <ul>
            <li class="home-link">
                <RouterLink to="/" class="router-link-custom"
                    >个人选品网站</RouterLink
                >
            </li>
            <div class="left-blocks">
                <li class="search">
                    <input v-model="query" />
                    <button @click="search">搜索</button>
                </li>
                <li class="shopping-cart">
                    <img src="/shopping-cart.png" alt="shopping cart" />
                </li>
                <li class="user-link">
                    <RouterLink
                        v-if="isLoggedIn"
                        to="/usercenter"
                        class="router-link-custom"
                        >user</RouterLink
                    >
                    <RouterLink v-else="" to="/login" class="router-link-custom"
                        >login</RouterLink
                    >
            </li>
        </div>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="HeadNav">
import { ref } from "vue";
import { RouterLink } from "vue-router";
import { useSearchStore } from "@/stores/index";
import type { URL } from "@/types";
import { initURL } from "@/types";

const query = ref<string>("");
const store = useSearchStore();
const isLoggedIn = true;

const checkLoginURL: URL = {
    proto: "http://",
    host: "localhost",
    port: 8000,
    url: "/api/user/logincheck",
    params: "",
};

// loginCheck
fetch(initURL(checkLoginURL))
    .then((response) => response.json())
    .then((res) => {
        console.log(res);
    });

function search() {
    // search
    const urlObj: URL = {
        proto: "http://",
        host: "localhost",
        port: 8000,
        url: "/api/items/search/",
        params: query.value,
    };

    if (urlObj.params == "") {
        urlObj.url = "/api/items/all";
    }

    const urlStr: string = initURL(urlObj);
    fetch(urlStr)
        .then((response) => response.json())
        .then((res) => {
            store.setResults(res);
        })
        .catch((error) => console.error(error));
}

</script>

<style>
.head-nav {
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    text-align: center;
    height: 80px;
    box-sizing: border-box;
}

.head-nav ul {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    list-style: none;
    background-color: #01000f;
    border: 2px solid #01000f;
    box-sizing: border-box;
}

.head-nav ul li:not(.search) {
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border: 2px solid #01000f;
    color: white;
    box-sizing: border-box;
}

.head-nav ul li:not(.search):hover {
    cursor: pointer;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border: 2px solid white;
    color: white;
    border-radius: 4px;
}

.shopping-cart img {
    padding: 0 20px;
}

.router-link-custom {
    display: flex;
    padding: 0 20px;
    flex-direction: column;
    justify-content: center;
    color: white;
    height: 100%;
    width: 100%;
    text-decoration: none;
}

.left-blocks {
    display: flex;
    flex-direction: row;
    height: 100%;
    justify-content: end;
    align-items: center;
}

.search {
    height: 50%;
    display: flex;
    flex-direction: row;
    border: #01000f solid 2px;
    border-radius: 3px;
}

.search:focus-within {
    border: #efeaaa solid 2px;
    border-radius: 6px;
    box-shadow: 1px 1px 10px 1px #efeaaa;
}

.search input {
    outline: none;
    height: 100%;
    border: none;
    border-radius: 3px 0px 0px 3px;
    padding-left: 8px;
}

.search button {
    padding: 0 10px;
    height: 100%;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    background-color: #3ff;
    border: none;
    color: black;
}

.search button:hover {
    cursor: pointer;
    background-color: #efeaaa;
}
</style>
