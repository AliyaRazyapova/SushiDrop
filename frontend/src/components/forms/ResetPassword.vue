<template>
  <div class="reset-password-container">
    <h1 class="reset-password-title">Сброс пароля</h1>
    <form @submit.prevent="resetPassword" class="reset-password-form">
      <label for="email" class="reset-password-label">Email:</label>
      <input type="email" id="email" v-model="email" required class="reset-password-input">
      <button type="submit" class="reset-password-button">Сбросить пароль</button>
    </form>
  </div>
</template>

<style scoped>
  .reset-password-title {
    color: #000000;
    font-size: 24px;
    margin-bottom: 20px;
    text-align: center;
  }

  .reset-password-form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .reset-password-label {
    color: #000000;
    margin-bottom: 10px;
  }

  .reset-password-input {
    width: 300px;
    padding: 10px;
    border: 1px solid #CCCCCC;
    border-radius: 4px;
    margin-bottom: 10px;
  }

  .reset-password-button {
    background-color: #F52341;
    color: #FFFFFF;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;

    font-size: 14px;
  }

  .reset-password-button:hover {
    background-color: #DD0000;
  }
</style>

<script>
export default {
  name: 'ResetPassword',
  data() {
    return {
      email: '',
    };
  },
  methods: {
    resetPassword() {
      fetch('http://localhost:8000/api/core/reset-password/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: this.email }),
      })
        .then(response => {
          if (response.ok) {
            alert('Password reset email sent.');
            this.email = '';
          } else {
            throw new Error('Failed to reset password.');
          }
        })
        .catch(error => {
          alert('Failed to reset password. Please try again.');
          console.error(error);
        });
    },
  },
};
</script>
