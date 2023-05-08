<template>
  <div class="register_form">
    <div class="title">
      Регистрация
    </div>
    <form @submit.prevent="registerUser">
      <div class="name_inp">
        <div class="name">
          Имя
        </div>
        <input type="first_name" class="inp inp_1" v-model="first_name" required>
      </div>
      <div class="name_inp">
        <div class="name">
          Почта
        </div>
        <input type="email" class="inp inp_1" v-model="email" required>
      </div>
      <div class="name_inp">
        <div class="name">
          Пароль
        </div>
        <input type="password" class="inp inp_1" v-model="password" required>
      </div>
      <div class="name_inp">
        <div class="name">
          Пароль (ещё раз)
        </div>
        <input type="password" class="inp" v-model="password_repeat" required>
        <div v-if="!passwordsMatch" class="smile passwords_mismatch">
          &#10060;
        </div>
        <div v-else class="smile passwords_match">
          &#10003;
        </div>
      </div>
      <div>
        <button type="submit" :disabled="!passwordsMatch">Register</button>
      </div>
    </form>
  </div>
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
.register_form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.name_inp {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.name {
  text-align: left;
}

.inp {
  text-align: right;
}

.inp_1 {
  margin-right: 20px;
}

.smile {
  width: 20px;
}

.passwords_match {
  color: green;
}
</style>
