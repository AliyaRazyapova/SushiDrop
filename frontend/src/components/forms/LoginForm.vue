<template>
  <div class="login-container">
    <div class="login-title">Вход</div>
    <form @submit.prevent="login" class="login-form">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div class="form-group">
        <label for="password">Пароль:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit" class="login-button">Войти</button>
    </form>
    <p v-if="message" class="login-message">{{ message }}</p>
    <VKForm />
  </div>
</template>

<script>
import axios from "axios";
import VKForm from "@/components/forms/VKForm";

export default {
  components: {
    VKForm
  },
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
          const token = response.data.token;
          this.message = "Вы успешно авторизовались!";
          localStorage.setItem("access_token", token);
          this.$router.push("/");
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

<style scoped>
  .login-container {
    text-align: center;
    max-width: 300px;
    margin: 90px auto 0 auto;
  }

  .login-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;

    color: black;
  }

  .login-form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .form-group {
    margin-bottom: 15px;
  }

  label {
    display: block;
    margin-bottom: 5px;

    color: black;
  }

  input[type="email"],
  input[type="password"] {
    width: 100%;
    padding: 4px 8px 4px 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  .login-button {
    padding: 8px 20px;
    background-color: #F52341;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;

    margin-bottom: 20px;
  }

  .login-message {
    margin-bottom: 20px;
  }
</style>
