import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from "@/components/pages/LoginPage";
import MainPage from "@/components/pages/MainPage";
import NaboryPage from "@/components/pages/NaboryPage";
import PremiumPage from "@/components/pages/PremiumPage";
import RollyISushiPage from "@/components/pages/RollyISushiPage";
import TempuraPage from "@/components/pages/TempuraPage";
import ZapechyonnyePage from "@/components/pages/ZapechyonnyePage";
import GoryacheeISalatyPage from "@/components/pages/GoryacheeISalatyPage";
import SousyPage from "@/components/pages/SousyPage";
import NapitkiIDesertyPage from "@/components/pages/NapitkiIDesertyPage";
import SpetsiiPage from "@/components/pages/SpetsiiPage";
import ProductProfile from "@/components/elements/ProductProfile";
import CartPage from "@/components/pages/CartPage";
import CreateProduct from "@/components/admin/CreateProduct";
import OrdersPage from "@/components/pages/OrdersPage";
import DiscountsList from "@/components/pages/DiscountsList";
import CreateDiscounts from "@/components/admin/CreateDiscounts";
import PasswordResetConfirmation from "@/components/forms/PasswordResetConfirmation.vue";
import RegistrationPage from "@/components/pages/RegistrationPage";
import ResetPassword from "@/components/forms/ResetPassword";
import UserProfilePage from "@/components/pages/UserProfilePage";
import EditProfilePage from "@/components/pages/EditProfilePage";

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainPage
  },
  {
    path: '/products/:productId',
    name: 'ProductProfile',
    component: ProductProfile,
    props: true
  },
  {
    path: '/products/create',
    name: 'CreateProduct',
    component: CreateProduct,
    props: true
  },
  {
    path: '/cart',
    name: 'CartPage',
    component: CartPage
  },
  {
    path: '/orders',
    name: 'OrdersPage',
    component: OrdersPage,
    props: true
  },
  {
    path: '/discounts',
    name: 'DiscountsList',
    component: DiscountsList
  },
  {
    path: '/discounts/add',
    name: 'CreateDiscounts',
    component: CreateDiscounts,
    props: true
  },
  {
    path: '/register',
    name: 'register',
    component: RegistrationPage
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage
  },
  {
    path: '/profile',
    name: 'UserProfilePage',
    component: UserProfilePage,
    meta: {
      requiresAuth: true,
    }
  },
  {
    path: '/profile/edit',
    name: 'EditProfilePage',
    component: EditProfilePage
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
  },
  {
    path: '/goryachee-i-salaty',
    name: 'goryachee-i-salaty',
    component: GoryacheeISalatyPage
  },
  {
    path: '/sousy',
    name: 'sousy',
    component: SousyPage
  },
  {
    path: '/napitki-i-deserty',
    name: 'napitki-i-deserty',
    component: NapitkiIDesertyPage
  },
  {
    path: '/spetsii',
    name: 'spetsii',
    component: SpetsiiPage
  },
  {
    path: '/reset-password',
    name: 'reset-password',
    component: ResetPassword
  },
  {
    path: '/reset-password-confirm/:uid/:token',
    name: 'reset-password-confirm',
    component: PasswordResetConfirmation
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
//
// function isLoggedIn() {
//   const token = localStorage.getItem('access_token');
//   if (token) {
//     try {
//       // Проверяем и декодируем JWT-токен
//       jwt.verify(token, 'django-insecure-tzndyj^x7-h!hkz*c+%i7*cez3y(0wrlx(dd7e^%=102%h0af0');
//       return true;
//     } catch (error) {
//       console.log('FUCK')
//       return false;
//     }
//   }
//   return false;
// }
//
//
// router.beforeEach((to, from, next) => {
//   if (to.meta.requiresAuth && !isLoggedIn()) {
//     next('/login');
//   } else {
//     next();
//   }
// });

export default router
