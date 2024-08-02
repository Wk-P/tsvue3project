<template>
    <LoginRegisterHeadNav />
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
                <input type="password" v-model="password1" autocomplete="off" />
            </div>
            <div><p class="sub-title">Re-enter password</p></div>
            <div class="sub-input">
                <input type="password" v-model="password2" autocomplete="off" />
            </div>
            <div class="button-group">
                <button @click="register">注册</button>
            </div>
        </form>
        <div class="login-register-link">
            <div>已有账户?</div>
            <RouterLink to="/login">登录</RouterLink>
        </div>
    </div>
</template>

<script lang="ts" setup name="register">
import { ref } from "vue";
import LoginRegisterHeadNav from "@/components/LoginRegisterHeadNav.vue";
import { getCSRFToken } from "@/utils/validate";

const username = ref<string>("");
const password1 = ref<string>("");
const password2 = ref<string>("");
const email = ref<string>("");

function register(event: Event) {
    event.preventDefault();

    getCSRFToken().then((csrftoken) => {
        // 检查输入是否合规
        if (username.value == "") {
            alert("请输入用户名");
            return;
        }

        if (password1.value == "" && password1.value == "") {
            alert("请输入密码");
            return;
        }

        if (password1.value != password2.value) {
            alert("两次输入密码不一致");
            return;
        }

        function isValidUsername(name: string) {
            const usernameRegex = /^[a-zA-Z0-9_]{3,20}$/;
            return usernameRegex.test(name);
        }

        function isValidEmail(email: string) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(email);
        }

        function isValidPassword(pswd: string) {
            const passwordRegex =
                /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
            return passwordRegex.test(pswd);
        }

        if (!isValidUsername(username.value)) {
            alert("名称格式不正确");
            return;
        }

        if (!isValidEmail(email.value)) {
            alert("邮箱格式不正确");
            return;
        }

        // test 密码不做检查
        const passwordTest = true;
        if (!passwordTest) {
            if (!isValidPassword(password1.value)) {
                alert("密码格式不正确");
                return;
            }
        }

        const url = "/backend/api/user/register";
        let params = "";

        if (params == "") {
            params += '/';
        }

        // 发起后端请求
        fetch(`${url}/${params}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
            },
            body: JSON.stringify({
                username: username.value,
                password: password1.value,
                email: email.value,
            }),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Register User Conflict");
                }
                return response.json();
            })
            .then((data) => {
                window.location.href = ('/');
            })
            .catch((error) => {
                console.error(error);
                alert(error.message);
            });
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
    padding: 0 15px;
    margin-left: 5px;
}

.login-register-link a:hover {
    color: #111;
}
</style>
