<template>
  <div class="buttons">
    <button v-if="isLoggedIn" @click="goToProfile">Профиль</button>
    <button v-else @click="goToRegister">Регистрация</button>
    <button v-if="isLoggedIn" class="button_1" @click="goToCart">Корзина</button>
    <button v-else @click="goToLogin">Войти</button>
  </div>
  <button v-if="isLoggedIn" @click="logout">Выйти</button>
</template>
<script>
export default {
  name: 'HeaderButtons',
  computed: {
    isLoggedIn() {
      return localStorage.getItem('access_token') !== null;
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
      localStorage.removeItem('access_token');
      this.$router.push('/');
      location.reload();
    },
    goToRegister() {
      this.$router.push('/register');
    }
  }
}
</script>

<style scoped>
.buttons {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;

  height: 24px;
  width: 230px;
}

button {
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  color: #F52341;
  background-color: transparent;

  display: flex;
  align-items: center;
  text-align: center;

  border: 1.5px solid #F52341;
  border-radius: 5px;

  padding: 0 14px;
  height: 28px;
  margin-top: 20px;
  margin-left: 24px;
}

.button_1 {
  margin-right: 10px;
}
</style>
