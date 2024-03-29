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
import CreateDiscounts from "@/components/admin/CreateDiscounts";
import PasswordResetConfirmation from "@/components/forms/PasswordResetConfirmation.vue";
import RegistrationPage from "@/components/pages/RegistrationPage";
import UserProfilePage from "@/components/pages/UserProfilePage";
import EditProfilePage from "@/components/pages/EditProfilePage";
import DiscountsPage from "@/components/pages/DiscountsPage";
import ResetPasswordPage from "@/components/pages/ResetPasswordPage";
import VKPage from "@/components/pages/VKPage";
import EditProduct from "@/components/admin/EditProduct";
import DiscountsForm from "@/components/admin/DiscountsForm";
import EditDiscounts from "@/components/admin/EditDiscounts";
import AdminPanel from "@/components/admin/AdminPanel";
import NewPasswordPage from "@/components/pages/NewPasswordPage";

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
    path: '/products/:productId/edit',
    name: 'EditProfile',
    component: EditProduct,
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
    name: 'DiscountsPage',
    component: DiscountsPage
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
    path: '/loginVk',
    name: 'loginVk',
    component: VKPage
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
    name: 'reset-password-page',
    component: ResetPasswordPage
  },
  {
    path: '/reset-password-confirm/:uid/:token',
    name: 'reset-password-confirm',
    component: PasswordResetConfirmation
  },
  {
    path: '/admin/discounts',
    name: 'discounts-form',
    component: DiscountsForm
  },
  {
    path: '/discounts/:discountId/edit',
    name: 'DiscountsEdit',
    component: EditDiscounts,
    props: true
  },
  {
    path: '/admin',
    name: 'AdminPanel',
    component: AdminPanel
  },
  {
    path: '/reset-password/:token',
    name: 'NewPasswordPage',
    component: NewPasswordPage,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
