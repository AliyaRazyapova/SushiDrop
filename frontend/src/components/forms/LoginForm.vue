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
      email: "",
      password: "",
      message: "",
    };
  },
  methods: {
    async login() {
      if (!this.email || !this.password) {
        this.message = "Заполните все поля";
        return;
      }

      const loginData = {
        email: this.email,
        password: this.password,
      };

      try {
        const response = await axios.post("http://localhost:8000/api/core/login/", loginData);

        if (response.status === 200) {
          const token = response.data.token; // Получение токена из ответа
          this.message = "Вы успешно авторизовались!";
          localStorage.setItem("access_token", token);
          this.$router.push("/profile/");
        }
      } catch (error) {
        if (error.response && error.response.data && error.response.data.error) {
          this.message = "Ошибка авторизации: " + error.response.data.error;
        } else {
          this.message = "Ошибка авторизации";
        }
      }
    },
  },
  created() {
    axios.interceptors.request.use((config) => {
      const token = localStorage.getItem("access_token");
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    });
  },
};
</script>
