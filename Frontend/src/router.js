import { createRouter, createWebHistory } from "vue-router";
import Login from "./components/Login.vue";
import Register from "./components/Register.vue";
import App from "./App.vue";
import Menu from "./components/Menu.vue";
import Slide from "./components/Slide.vue";
import Ticket from "./components/Ticket.vue";
import AdminPanel from "./components/AdminPanel.vue";
import Food from "./components/Food.vue";



export default createRouter({
    history: createWebHistory(),
    routes: [
    { path: '/', redirect: '/register' },
    {path: '/register', component: Register},
    {path: '/login', component: Login},
    {path: '/menu', component: Menu},
    {path: '/slide', component: Slide},
    {path: "/ticket", component: Ticket},
    {path: "/admin", component: AdminPanel},
    {path: "/food", component: Food}
    ]
})