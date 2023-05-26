<template>
  <div>
    <hea-der />
    <category-list />
    <user-profile />
    <button v-if="isAdmin" class="admin-button"
            @click="goToAdminPanel">Административная панель</button>
  </div>
</template>

<script>
import UserProfile from "@/components/elements/UserProfile";
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";
import axios from "axios";

export default {
  name: "UserProfilePage",
  components: { CategoryList, HeaDer, UserProfile },
  data() {
    return {
      isAdmin: false,
    };
  },
  mounted() {
    this.checkAdminStatus();
  },
  methods: {
    async checkAdminStatus() {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get('http://localhost:8000/api/core/auth/', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });

        if (response.data.role) {
          this.isAdmin = true;
        }
      } catch (error) {
        console.error(error);
      }
    },
    goToAdminPanel() {
      this.$router.push('/admin')
    },
  },
};
</script>

<style scoped>
 .admin-button {
    background-color: #F52341;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
</style>