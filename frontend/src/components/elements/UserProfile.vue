<template>
  <div class="container">
    <h2>Личный кабинет</h2>
    <div v-if="loading" class="loading">Загрузка...</div>
    <div v-else>
      <div class="field">
        <span class="field-label">Email:</span>
        <span class="field-value">{{ user.email || 'null' }}</span>
      </div>
      <div class="field">
        <span class="field-label">Имя:</span>
        <span class="field-value">{{ user.first_name || 'null' }}</span>
      </div>
      <div class="field">
        <span class="field-label">Фамилия:</span>
        <span class="field-value">{{ user.last_name || 'null' }}</span>
      </div>
      <div class="field">
        <span class="field-label">Номер телефона:</span>
        <span class="field-value">{{ user.phone_number || 'null' }}</span>
      </div>
      <div class="field">
        <span class="field-label">Адрес:</span>
        <span class="field-value">{{ user.address || 'null' }}</span>
      </div>
      <button @click="editProfile" class="edit-button">Редактировать</button>
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
      const token = localStorage.getItem('access_token');
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
    editProfile() {
      this.$router.push('/profile/edit/');
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

h2 {
  font-size: 24px;
  margin-top: 40px;
  margin-bottom: 40px;
  color: #000000;
}

.loading {
  margin-top: 20px;
  font-style: italic;
  color: #000000;
}

.field {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.field-label {
  font-weight: bold;
  color: #000000;
}

.field-value {
  text-align: right;
  color: #595959;
}

.edit-button {
  padding: 5px 10px;
  background-color: #F52341;
  color: #ffffff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  margin-top: 40px;
}

.edit-button:hover {
  background-color: #cc0000;
}
</style>
