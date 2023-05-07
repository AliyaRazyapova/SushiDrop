<template>
  <form @submit.prevent="registerUser">
    <div>
      <label for="email">Email:</label>
      <input type="email" id="email" v-model="email" required>
    </div>
    <div>
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required>
    </div>
    <div>
      <label for="firstName">First name:</label>
      <input type="text" id="firstName" v-model="firstName" required>
    </div>
    <div>
      <label for="lastName">Last name:</label>
      <input type="text" id="lastName" v-model="lastName" required>
    </div>
    <div>
      <label for="phoneNumber">Phone number:</label>
      <input type="text" id="phoneNumber" v-model="phoneNumber" required>
    </div>
    <div>
      <label for="address">Address:</label>
      <input type="text" id="address" v-model="address" required>
    </div>
    <div v-if="error">{{ error }}</div>
    <button type="submit">Register</button>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegistrationForm',
  data() {
    return {
      email: '',
      password: '',
      firstName: '',
      lastName: '',
      phoneNumber: '',
      address: '',
      error: '',
    };
  },
  methods: {
    async registerUser() {
      try {
        const response = await axios.post('/api/core/register/', {
          email: this.email,
          password: this.password,
          first_name: this.firstName,
          last_name: this.lastName,
          phone_number: this.phoneNumber,
          address: this.address,
        });
        console.log(response.data);
      } catch (error) {
        console.error(error);
        this.error = 'Error registering user';
      }
    },
  },
};
</script>
