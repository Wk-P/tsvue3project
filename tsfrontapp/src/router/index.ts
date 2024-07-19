import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/home/App.vue";
import Login from "@/pages/login/App.vue";
import Register from "@/pages/register/App.vue";
import Product from "@/pages/product/App.vue";
import Comments from "@/pages/comments/App.vue";
import Details from "@/pages/details/App.vue";
import UserCenter from "@/pages/usercenter/App.vue"
import Orders from "@/pages/orders/App.vue";
import Cart from "@/pages/cart/App.vue";
import Favorite from "@/pages/favorite/App.vue"

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
                path: "details",
                name: "details",
                component: Details,
            },
            {
                path: "comments",
                name: "comments",
                component: Comments,
            },
        ],
    },
    {
        path: "/usercenter",
        name: "usercenter",
        component: UserCenter,
        redirect: { name: 'orders' }, // 设置默认路由重定向
        children: [
            {
                path: "orders",
                name: "orders",
                component: Orders,
            },
            {
                path: "favorite",
                name: "favorite",
                component: Favorite,
            },
            {
                path: "cart",
                name: "cart",
                component: Cart,
            },
        ]
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
