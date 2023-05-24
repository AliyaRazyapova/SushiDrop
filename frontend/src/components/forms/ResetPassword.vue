<template>
  <div>
    <h1>Reset Password</h1>
    <form @submit.prevent="resetPassword">
      <label htmlFor="email">Email:</label>
      <input type="email" id="email" v-model="email" required>
      <button type="submit">Reset Password</button>
    </form>
  </div>
</template>

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
