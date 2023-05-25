<template>
  <div class="container">
    <h2>Редактирование профиля</h2>
    <form @submit.prevent="updateProfile" class="edit-form">
      <div class="form-group">
        <label for="first_name" class="label-left">Имя:</label>
        <input type="text" id="first_name" v-model="user.first_name" required class="input-right">
      </div>
      <div class="form-group">
        <label for="last_name" class="label-left">Фамилия:</label>
        <input type="text" id="last_name" v-model="user.last_name" required class="input-right">
      </div>
      <div class="form-group">
        <label for="phone_number" class="label-left">Номер телефона:</label>
        <input type="text" id="phone_number" v-model="user.phone_number" required class="input-right">
      </div>
      <div class="form-group">
        <label for="address" class="label-left">Адрес:</label>
        <input type="text" id="address" v-model="user.address" required class="input-right">
      </div>
      <div class="form-group">
        <button type="submit" class="save-button">Сохранить</button>
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

<style scoped>
  .container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
  }

  h2 {
    font-size: 24px;
    margin-bottom: 40px;
  }

  .edit-form {
    display: flex;
    flex-direction: column;
  }

  .form-group {
    margin-bottom: 10px;
  }

  .label-left {
    text-align: left;
    font-weight: bold;
    display: inline-block;
    width: 150px;
  }

  .input-right {
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 3px;
    text-align: right;
    display: inline-block;
    width: 200px;
  }

  .save-button {
    padding: 5px 10px;
    background-color: #F52341;
    color: #fff;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    margin-top: 20px;

    font-size: 14px;
  }

  .save-button:hover {
    background-color: #F52341;
  }
</style>
