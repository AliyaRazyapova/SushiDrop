import { createRouter, createWebHistory } from 'vue-router'
import RegistrationForm from "@/components/forms/RegistrationForm";
import LoginForm from "@/components/forms/LoginForm";
import HeaDer from "@/components/elements/HeaDer";
import UserProfile from "@/components/forms/UserProfile";

const routes = [
  {
    path: '/',
    name: 'main',
    component: HeaDer
  },
  {
    path: '/register',
    name: 'register',
    component: RegistrationForm
  },
  {
    path: '/login',
    name: 'login',
    component: LoginForm
  },
  {
    path: '/profile',
    name: 'profile',
    component: UserProfile
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
