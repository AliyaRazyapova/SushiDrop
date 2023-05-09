<template>
  <div class="register_form">
    <div class="title inp_1">
      Регистрация
    </div>
    <form @submit.prevent="registerUser">
      <div class="name_inp">
        <div class="name">
          Имя
        </div>
        <input type="text" class="inp inp_1" placeholder="Введите своё имя" v-model="first_name" required>
      </div>
      <div class="name_inp">
        <div class="name">
          Почта
        </div>
        <input type="email" class="inp inp_1" placeholder="Введите свою почту" v-model="email" required>
      </div>
      <div class="name_inp">
        <div class="name">
          Пароль
        </div>
        <input type="password" class="inp inp_1" placeholder="Введите пароль" v-model="password" required>
      </div>
      <div class="name_inp">
        <div class="name">
          Пароль (ещё раз)
        </div>
        <input type="password" class="inp" placeholder="Введите пароль повторно" v-model="password_repeat" required>
        <div v-if="!passwordsMatch" class="smile passwords_mismatch">
          &#10060;
        </div>
        <div v-else class="smile passwords_match">
          &#10003;
        </div>
      </div>
      <div>
        <button class="button inp_1" type="submit" :disabled="!passwordsMatch">
          Зарегистрироваться
        </button>
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
        this.$router.push('/');
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

.title {
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: 600;
  font-size: 24px;
  line-height: 36px;
  color: #212121;

  margin-bottom: 54px;
}

.name_inp {
  display: flex;
  flex-direction: row;
  justify-content: space-between;

  margin-bottom: 18px;
}

.name {
  text-align: left;
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 15px;
  color: #000000;

  padding: 4px;
}

.inp {
  width: 216px;
  height: 24px;
  border: 1.3px solid #939393;
  border-radius: 3px;

  margin-left: 30px;
  padding-left: 10px;
}

.inp::placeholder {
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 12px;
  line-height: 18px;
  color: #A6A6A6;

  padding-left: 3px;
}

.inp_1 {
  margin-right: 30px;
}

.smile {
  padding-top: 4px;
  width: 30px;
}

.passwords_match {
  color: green;
}

.button {
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 17px;

  color: #FAFAFA;
  background: #E30538;
  border-radius: 4px;
  border: 1px solid #FAFAFA;

  width: 131px;
  height: 27px;

  margin-top: 8px;
}
</style>
