<template>
  <div>
    <h2>Вход в систему</h2>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div>
        <label for="password">Пароль:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">Войти</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      email: '',
      password: '',
      message: '',
    }
  },
  methods: {
    async login() {
      try {
        const response = await axios.post(
            'http://localhost:8000/api/core/login/', {
              email: this.email,
              password: this.password
            })
        if (response.status === 200) {
          this.message = 'Вы успешно авторизовались!'
          localStorage.setItem('token', response.data.token)
          this.$router.push('/home')
        }
      } catch (error) {
        this.message = 'Ошибка авторизации: ' + error.response.data.message
      }
    }
  }
}
</script>