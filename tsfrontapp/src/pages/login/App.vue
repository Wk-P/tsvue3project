<template>
    <LoginRegisterHeadNav />
    <div class="block">
        <h2 class="title">登录</h2>
        <form>
            <div>
                <p class="sub-title">Email or ID</p>
            </div>
            <div class="sub-input">
                <input type="text" v-model="username" />
            </div>
            <div>
                <p class="sub-title">Password</p>
            </div>
            <div class="sub-input">
                <input type="password" v-model="password" autocomplete="on" />
            </div>
            <div class="button-group"><button @click="login">登录</button></div>
        </form>
        <div class="login-register-link">
            <div>还没账户?</div>
            <RouterLink to="/register">注册</RouterLink>
        </div>
    </div>
</template>

<script lang="ts" setup name="login">
import { ref } from "vue";
import { RouterLink } from "vue-router";
import { useRouter } from "vue-router";
import { userTokenStore } from "@/stores/index";
import { getCSRFToken } from "@/utils/validate";

import LoginRegisterHeadNav from "@/components/LoginRegisterHeadNav.vue";

const tokenStore = userTokenStore();
const router = useRouter();
const username = ref("");
const password = ref("");

async function login(event: Event) {
    event.preventDefault();

    getCSRFToken().then((csrfToken) => {
        if (csrfToken === null) {
            throw new Error("Invalid Token");
        }

        const url = "/backend/api/user/login";
        let params = "";

        if (params == '') {
            params += '/';
        }

        // 向后端Token处理器发出请求
        fetch(`${url}/${params}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken,
            },
            body: JSON.stringify({
                username: username.value,
                password: password.value,
            }),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Authentication Invalid");
                }
                return response.json();
            })
            .then((data) => {
                // save token and into pinia
                tokenStore.setToken(csrfToken, username.value);
                router.push("/");
            })
            .catch((error) => {
                console.error(error);
                alert(error.message);
            });
    }).catch(error => {
        console.error(error.message);
    })
}
</script>
<style scoped>
.block {
    border-radius: 10px 10px 0 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 20px auto 50px auto;
}

.title {
    width: 30%;
    border-radius: 10px;
    margin: 40px 0;
}

form {
    width: 30%;
    background-color: #fffffe;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px 80px;
    border-radius: 10px;
}

form div {
    margin-top: 2px;
    width: 100%;
}

.sub-title {
    margin-top: 20px;
    font-weight: bold;
}

.sub-input input {
    width: 100%;
    height: 30px;
    outline: none;
    border-radius: 4px;
    border: 1px solid #444;
    padding: 2px 10px;
    transition: all 0.3s ease-out;
    box-sizing: border-box;
}

.sub-input input:focus {
    box-shadow: 0 0 5px 2px skyblue;
}

.button-group {
    width: 100%;
    margin: 35px 0;
}

.button-group button {
    width: 100%;
    outline: none;
    border: none;
    border-radius: 4px;
    padding: 10px 0;
    background-color: rgb(255, 200, 0);
    transition: box-shadow 0.2s ease;
}

.button-group button:hover {
    box-shadow: 0 0 10px 2px rgb(255, 200, 0);
    cursor: pointer;
}

.login-register-link {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin: 20px auto;
}

.login-register-link a {
    color: #555;
    text-decoration: none;
    text-align: center;
    padding: 0 15px;
    margin-left: 5px;
}

.login-register-link a:hover {
    color: #111;
}
</style>
