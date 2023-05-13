import { createRouter, createWebHistory } from 'vue-router'
import RegistrationForm from "@/components/forms/RegistrationForm";
import LoginForm from "@/components/forms/LoginForm";
import UserProfile from "@/components/forms/UserProfile";
import MainPage from "@/components/pages/MainPage";
import NaboryPage from "@/components/pages/NaboryPage";
import PremiumPage from "@/components/pages/PremiumPage";
import RollyISushiPage from "@/components/pages/RollyISushiPage";
import TempuraPage from "@/components/pages/TempuraPage";
import ZapechyonnyePage from "@/components/pages/ZapechyonnyePage";

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
    path: '/nabory',
    name: 'nabory',
    component: NaboryPage
  },
  {
    path: '/premium',
    name: 'premium',
    component: PremiumPage
  },
  {
    path: '/rolly-i-sushi',
    name: 'rolly-i-sushi',
    component: RollyISushiPage
  },
  {
    path: '/tempura',
    name: 'tempura',
    component: TempuraPage
  },
  {
    path: '/zapechyonnye',
    name: 'zapechyonnye',
    component: ZapechyonnyePage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
