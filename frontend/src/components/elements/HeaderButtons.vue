<template>
  <div class="buttons">
    <button v-if="isLoggedIn" @click="goToProfile">Профиль</button>
    <button v-else @click="goToLogin">Войти</button>
    <button @click="goToCart">Корзина</button>
  </div>
  <button v-if="isLoggedIn" @click="logout">Выйти</button>
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

<style scoped>
.buttons {
  display: flex;
  flex-direction: row;
}

button {
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: 600;
  font-size: 12px;
  line-height: 18px;
  color: #F52341;
  background-color: transparent;

  display: flex;
  align-items: center;
  text-align: center;

  border: 1px solid #F52341;
  border-radius: 5px;

  padding: 3px 10px;
}
</style>
