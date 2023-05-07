import { createRouter, createWebHistory } from 'vue-router'
import RegistrationForm from "@/components/RegistrationForm";

const routes = [
  {
    path: '/register',
    name: 'register',
    component: RegistrationForm
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
