import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/home/App.vue";
import Login from "@/pages/login/App.vue";
import Register from "@/pages/register/App.vue";
import Product from "@/pages/product/App.vue";
import Comments from "@/pages/comments/App.vue";
import Details from "@/pages/details/App.vue";
import UserCenter from "@/pages/usercenter/App.vue"

const routes = [
    {
        path: "/",
        name: "home",
        component: Home,
    },
    {
        path: "/login",
        name: "login",
        component: Login,
    },
    {
        path: "/register",
        name: "register",
        component: Register,
    },
    {
        path: "/product/:productId",
        name: "product",
        component: Product,
        children: [
            {
                path: "/product/:productId/details",
                name: "details",
                component: Details,
            },
            {
                path: "/product/:productId/comments",
                name: "comments",
                component: Comments,
            },
        ],
    },
    {
        path: "/usercenter",
        name: "usercenter",
        component: UserCenter,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
