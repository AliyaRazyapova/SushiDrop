<template>
  <div className="reset-password-confirm-container">
    <h1 className="reset-password-confirm-title">Выберите новый пароль</h1>
    <form @submit.prevent="confirmPasswordReset" class="reset-password-confirm-form">
      <label htmlFor="password" className="reset-password-confirm-label">Новый пароль:</label>
      <input type="password" id="password" v-model="password" required className="reset-password-confirm-input">
      <button type="submit" className="reset-password-confirm-button">Сохранить пароль</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'NewPassword',
  data() {
    return {
      password: '',
    };
  },
  methods: {
    confirmPasswordReset() {
      const token = this.$route.params.token;
      console.log(token)
      fetch(`http://localhost:8000/api/core/reset-password/${token}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({password: this.password}),
      })
          .then(response => {
            console.log(response)
            if (response.ok) {
              alert('Password reset successful.');
              this.password = '';
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
