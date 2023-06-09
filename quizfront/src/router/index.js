import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/tmp',
    name: 'tmp',
    component: () => import('../views/Tmp.vue')
  },
  {
    path: '/exam',
    name: 'exam',
    component: () => import('../views/Exam.vue')
  },
  {
    path: '/practice',
    name: 'practice',
    component: () => import('../views/Practice.vue')
  },
  {
    // path: '/about',
    // name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
