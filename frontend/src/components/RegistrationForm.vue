<template>
  <div class="title">
    Регистрация
  </div>
  <form @submit.prevent="registerUser">
    <div>
      <label for="first_name">
        Имя
      </label>
      <input type="first_name" id="first_name" v-model="first_name" required>
    </div>
    <div>
      <label for="email">
        Почта
      </label>
      <input type="email" id="email" v-model="email" required>
    </div>
    <div>
      <label for="password">
        Пароль
      </label>
      <input type="password" id="password" v-model="password" required>
    </div>
    <div>
      <label for="password_repeat">
        Пароль (ещё раз)
      </label>
      <input type="password" id="password_repeat" v-model="password_repeat" required>
      <div v-if="!passwordsMatch" class="passwords_mismatch">
        &#10060;
      </div>
      <div v-else class="passwords_match">
        &#10003;
      </div>
    </div>
    <div>
      <button type="submit" :disabled="!passwordsMatch">Register</button>
    </div>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      first_name: '',
      email: '',
      password: '',
      password_repeat: ''
    }
  },
  computed: {
    passwordsMatch() {
      return this.password === this.password_repeat;
    }
  },
  methods: {
    async registerUser() {
      try {
        const response = await axios.post('http://localhost:8000/api/core/register/', {
          first_name: this.first_name,
          email: this.email,
          password: this.password
        });
        console.log(response.data);
      } catch (error) {
        console.log(error);
      }
    }
  }
}
</script>

<style>
.passwords_match {
  color: green;
}
</style>
