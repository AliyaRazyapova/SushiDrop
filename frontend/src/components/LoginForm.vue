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
    <div>
    <button @click="authorize">Авторизация через VK</button>
  </div>
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
          this.$router.push('/')
        }
      } catch (error) {
        this.message = 'Ошибка авторизации: ' + error.response.data.message
      }
    },
    authorize() {
      const vkAuthUrl = `https://oauth.vk.com/authorize?client_id=51639163&redirect_uri=http://localhost:8000/auth/vk/callback&response_type=code&scope=email`;

      window.location.href = vkAuthUrl;

      window.addEventListener('message', async (event) => {
        if (event.origin !== 'https://oauth.vk.com') {
          return;
        }

        const code = event.data.code;
        const tokenResponse = await axios.post(`https://oauth.vk.com/access_token?client_id=51639163&client_secret=N2eKlfa7qpe7NC20car5&redirect_uri=http://localhost:8000/auth/vk/callback&code=${code}`);
        const userResponse = await axios.get(`https://api.vk.com/method/users.get?fields=email&access_token=${tokenResponse.data.access_token}&v=5.130&lang=en`);

        console.log(userResponse.data.response[0]);
      });
    }
  }
}
</script>