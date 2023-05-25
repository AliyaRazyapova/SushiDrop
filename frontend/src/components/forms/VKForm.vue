<template>
  <div>
    <input type="email" v-model="email" name="email" placeholder="Введите ваш email">
    <button class="vk-button" @click="authorize">Авторизация через VK</button>
  </div>
</template>

<script>
export default {
  name: "VKForm",
  data() {
    return {
      email: ""
    };
  },
  methods: {
    authorize() {
      const vkAuthUrl = `https://oauth.vk.com/authorize?client_id=51639163&redirect_uri=http://localhost:8000/auth/vk/callback&response_type=code&scope=email&state=${encodeURIComponent(this.email)}`;
      window.location.href = vkAuthUrl;
    }
  },
  mounted() {
    const params = new URLSearchParams(window.location.search);
    const jwtToken = params.get('jwt_token');

    if (jwtToken) {
      localStorage.setItem('access_token', jwtToken);
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>
.vk-button {
  padding: 7px 20px;
  background-color: #4A76A8;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.vk-button:hover {
  background-color: #375E91;
}
</style>


