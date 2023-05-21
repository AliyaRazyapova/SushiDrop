<template>
  <div>
    <h2>Edit Profile</h2>
    <form @submit.prevent="updateProfile">
      <div>
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" v-model="user.first_name" required>
      </div>
      <div>
        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" v-model="user.last_name" required>
      </div>
      <div>
        <label for="phone_number">Phone Number:</label>
        <input type="text" id="phone_number" v-model="user.phone_number" required>
      </div>
      <div>
        <label for="address">Address:</label>
        <input type="text" id="address" v-model="user.address" required>
      </div>
      <div>
        <button type="submit">Save</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'EditProfile',
  data() {
    return {
      user: {
        first_name: '',
        last_name: '',
        phone_number: '',
        address: ''
      }
    };
  },
  mounted() {
    this.fetchUserProfile();
  },
  methods: {
    fetchUserProfile() {
      const token = localStorage.getItem('access_token');
      axios
        .get('http://localhost:8000/api/core/profile/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then(response => {
          this.user = response.data;
        })
        .catch(error => {
          console.log('Failed to fetch user profile', error);
        });
    },
    updateProfile() {
      const token = localStorage.getItem('access_token');
      axios
        .put('http://localhost:8000/api/core/profile/', this.user, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then(() => {
          console.log('Profile updated successfully');
          this.$router.push('/profile');
        })
        .catch(error => {
          console.log('Failed to update profile', error);
        });
    },
  },
};
</script>
