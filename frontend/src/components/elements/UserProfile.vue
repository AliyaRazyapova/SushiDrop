<template>
  <div>
    <h2>User Profile</h2>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <p>Email: {{ user.email }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'UserProfile',
  data() {
    return {
      loading: true,
      user: null,
    };
  },
  mounted() {
    this.fetchUserProfile();
  },
  methods: {
    fetchUserProfile() {
      const token = localStorage.getItem('access_token')
      console.log(token)
      axios
        .get('http://localhost:8000/api/core/profile/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then(response => {
          this.user = response.data;
          this.loading = false;
        })
        .catch(error => {
          console.log('Failed to fetch user profile', error);
          this.loading = false;
        });
    },
  },
};
</script>
