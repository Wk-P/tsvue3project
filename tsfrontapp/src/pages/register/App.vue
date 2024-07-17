<template>
    <LoginRegisterHeadNav/>
    <div class="block">
        <h2 class="title">注册</h2>
        <form>
            <div><p class="sub-title">Your name</p></div>
            <div class="sub-input">
                <input type="text" v-model="username" />
            </div>
            <div><p class="sub-title">Email</p></div>
            <div class="sub-input">
                <input type="email" v-model="email" />
            </div>
            <div><p class="sub-title">Password</p></div>
            <div class="sub-input">
                <input type="password" v-model="password1" autocomplete="off"/>
            </div>
            <div><p class="sub-title">Re-enter password</p></div>
            <div class="sub-input">
                <input type="password" v-model="password2" autocomplete="off"/>
            </div>
            <div class="button-group"><button @click="register">注册</button></div>
        </form>
        <div class="login-register-link">
            <div>已有账户?</div><RouterLink to="/login">登录</RouterLink>
        </div>
    </div>
</template>

<script lang="ts" setup name="register">
import { ref } from "vue";
import type { URL } from "@/types/index";
import { initURL } from "@/types/index";
import LoginRegisterHeadNav from "@/components/LoginRegisterHeadNav.vue";

const username = ref("");
const password1 = ref("");
const password2 = ref("");
const email = ref("");
const enableRegister = ref(false);

async function register() {
    // 构造访问路径
    const loginURLObj: URL = {
        proto: "http://",
        host: "localhost",
        port: 8000,
        url: "/user/login",
        params: "",
    };
    const loginURL: string = initURL(loginURLObj);

    // 检查输入是否合规
    if (username.value == "") {
        alert("请输入用户名");
        return;
    } else {
        if (password1.value == "" && password1.value == "") {
            alert("请输入密码");
            return;
        } else if (password1.value != password2.value) {
            alert("两次输入密码不一致");
            return;
        }
    }

    if (!enableRegister.value) {
        alert("请先检查用户名");
        return;
    }
    

    // 发起后端请求
    fetch(loginURL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username: username.value,
            email: email.value,
            password: password1.value,
        }),
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            
        });
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
    padding-left: 15px;
}

.login-register-link a:hover {
    color: #111;
}
</style>
