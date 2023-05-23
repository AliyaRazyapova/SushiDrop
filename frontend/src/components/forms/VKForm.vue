<template>
  <button @click="authorize">Авторизация через VK</button>
</template>

<script>
export default {
  name: "VKForm",
  methods: {
    authorize() {
      const vkAuthUrl = `https://oauth.vk.com/authorize?client_id=51639163&redirect_uri=http://localhost:8000/auth/vk/callback&response_type=code&scope=email`;
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


