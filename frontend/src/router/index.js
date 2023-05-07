import { createRouter, createWebHistory } from 'vue-router'
import RegistrationForm from "@/components/RegistrationForm";
import LoginForm from "@/components/LoginForm";

const routes = [
  {
    path: '/register',
    name: 'register',
    component: RegistrationForm
  },
  {
    path: '/login',
    name: 'login',
    component: LoginForm
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
