import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/about',
        name: 'about',
        component: () => import('../views/About')
    },
    {
        path: '/user',
        name: 'user',
        component: () => import('../views/user/User'),
        children: [
            {
                path: '',
                name: 'userProfile',
                component: () => import('../views/user/Profile')
            },
            {
                path: 'Register',
                name: 'userRegister',
                component: () => import('../views/user/Register')
            },
        ]
    },
    {
        path: '/user/autologin',
        name: 'userAutoLogin',
        component: () => import('../views/user/AutoLogin')
    },
    {
        path: '/user/login',
        name: 'userLogin',
        component: () => import('../views/user/Login')
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
