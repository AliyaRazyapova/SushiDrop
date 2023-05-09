<template>
  <div>
    <button v-if="isLoggedIn" @click="goToProfile">Профиль</button>
    <button v-else @click="goToLogin">Войти</button>
    <button @click="goToCart">Корзина</button>
    <button v-if="isLoggedIn" @click="logout">Выйти</button>
  </div>
</template>

<script>
export default {
  name: 'HeaderButtons',
  computed: {
    isLoggedIn() {
      return localStorage.getItem('token') !== null;
    }
  },
  methods: {
    goToProfile() {
      this.$router.push('/profile');
    },
    goToCart() {
      this.$router.push('/cart');
    },
    goToLogin() {
      this.$router.push('/login');
    },
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/');
      location.reload();
    }
  }
}
</script>
