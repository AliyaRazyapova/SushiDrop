import { createRouter, createWebHistory } from 'vue-router'
import RegistrationForm from "@/components/forms/RegistrationForm";
import LoginForm from "@/components/forms/LoginForm";
import UserProfile from "@/components/forms/UserProfile";
import MainPage from "@/components/pages/MainPage";
import PremiumPage from "@/components/pages/PremiumPage";

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainPage
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
  },
  {
    path: '/premium',
    name: 'premium',
    component: PremiumPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
