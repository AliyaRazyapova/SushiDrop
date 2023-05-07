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
      <label for="firstName">First Name:</label>
      <input type="text" id="firstName" v-model="firstName" required>
    </div>
    <div>
      <label for="lastName">Last Name:</label>
      <input type="text" id="lastName" v-model="lastName" required>
    </div>
    <div>
      <label for="phoneNumber">Phone Number:</label>
      <input type="text" id="phoneNumber" v-model="phoneNumber">
    </div>
    <div>
      <label for="address">Address:</label>
      <input type="text" id="address" v-model="address">
    </div>
    <div>
      <button type="submit">Register</button>
    </div>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      firstName: '',
      lastName: '',
      phoneNumber: '',
      address: ''
    }
  },
  methods: {
    async registerUser() {
      try {
        const response = await axios.post('http://localhost:8000/api/core/register/', {
          email: this.email,
          password: this.password,
          first_name: this.firstName,
          last_name: this.lastName,
          phone_number: this.phoneNumber,
          address: this.address
        });
        console.log(response.data);
      } catch (error) {
        console.log(error);
      }
    }
  }
}
</script>
