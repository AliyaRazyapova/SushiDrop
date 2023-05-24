<template>
  <div>
    <h1>Confirm Password Reset</h1>
    <form @submit.prevent="confirmPasswordReset">
      <label for="new-password">New Password:</label>
      <input type="password" id="new-password" v-model="newPassword" required>
      <button type="submit">Confirm Reset</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PasswordResetConfirm',
  data() {
    return {
      newPassword: '',
    };
  },
  methods: {
    confirmPasswordReset() {
      const uid = this.$route.params.uid;
      const token = this.$route.params.token;

      axios.post('http://localhost:8000/api/core/reset-password-confirm/', { uid, token, new_password: this.newPassword })
        .then(() => {
          alert('Password reset successful.');
          this.newPassword = '';
        })
        .catch(error => {
          alert('Failed to reset password. Please try again.');
          console.error(error);
        });
    },
  },
};
</script>