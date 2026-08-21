import { createRouter, createWebHistory } from "vue-router";
import Login from "./components/Login.vue";
import Register from "./components/Register.vue";
import App from "./App.vue";
import Menu from "./components/Menu.vue";
import Slide from "./components/Slide.vue";



export default createRouter({
    history: createWebHistory(),
    routes: [
    { path: '/', redirect: '/register' },
    {path: '/register', component: Register},
    {path: '/login', component: Login},
    {path: '/menu', component: Menu},
    {path: '/slide', component: Slide}
    ]
})