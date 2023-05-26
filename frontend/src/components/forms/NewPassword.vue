<template>
  <div class="reset-password-confirm-container">
    <h1 class="reset-password-confirm-title">Выберите новый пароль</h1>
    <form @submit.prevent="confirmPasswordReset" class="reset-password-confirm-form">
      <label for="password" class="reset-password-confirm-label">Новый пароль:</label>
      <input type="password" id="password" v-model="password" required class="reset-password-confirm-input">

      <label for="confirm-password" class="reset-password-confirm-label">Подтвердите новый пароль:</label>
      <input type="password" id="confirm-password" v-model="confirmPassword" required class="reset-password-confirm-input">
      <p v-if="password !== confirmPassword" class="password-mismatch-message">Пароли не совпадают.</p>

      <div class="button-container">
        <button type="submit" class="reset-password-confirm-button">Сохранить пароль</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'NewPassword',
  data() {
    return {
      password: '',
      confirmPassword: '',
    };
  },
  methods: {
    confirmPasswordReset() {
      const token = this.$route.params.token;
      console.log(token);

      if (this.password !== this.confirmPassword) {
        alert('Пароли не совпадают.');
        return;
      }

      fetch(`http://localhost:8000/api/core/reset-password/${token}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ password: this.password }),
      })
        .then(response => {
          console.log(response);
          if (response.ok) {
            alert('Смена пароля прошла успешно.');
            this.password = '';
            this.confirmPassword = '';
            // this.$router.push('/');
          } else {
            throw new Error('Не удалось сменить пароль.');
          }
        })
        .catch(error => {
          alert('Не удалось сменить пароль. Пожалуйста, попробуйте снова.');
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
  .reset-password-confirm-container {
    text-align: center;
    margin-top: 50px;
  }

  .reset-password-confirm-title {
    color: #000000;
    font-size: 24px;
  }

  .reset-password-confirm-form {
    margin-top: 20px;
  }

  .reset-password-confirm-label {
    display: block;
    margin-bottom: 5px;
  }

  .reset-password-confirm-input {
    width: 300px;
    padding: 5px;
    margin-bottom: 10px;
  }

  .password-mismatch-message {
    color: #000000;
    font-size: 14px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .reset-password-confirm-button {
    padding: 10px 20px;
    background-color: #F52341;
    color: white;
    border: none;
    cursor: pointer;
  }

  .button-container {
    margin-top: auto;
    display: flex;
    justify-content: center;
  }
</style>
