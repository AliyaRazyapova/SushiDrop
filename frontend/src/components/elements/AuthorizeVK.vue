<template>
  <button @click="authorize">Войти через VK</button>
</template>

<script>
import axios from "axios";

export default {
  name: "AuthorizeVK",
  methods: {
    authorize() {
      const vkAuthUrl = `https://oauth.vk.com/authorize?client_id=51639163&redirect_uri=http://localhost:8000/auth/vk/callback&response_type=code&scope=email`;

      window.location.href = vkAuthUrl;

      window.addEventListener('message', async (event) => {
        if (event.origin !== 'https://oauth.vk.com') {
          return;
        }

        const code = event.data.code;
        const tokenResponse = await axios.post(`https://oauth.vk.com/access_token?client_id=51639163&client_secret=N2eKlfa7qpe7NC20car5&redirect_uri=http://localhost:8000/auth/vk/callback&code=${code}`);
        const userResponse = await axios.get(`https://api.vk.com/method/users.get?fields=email&access_token=${tokenResponse.data.access_token}&v=5.130&lang=en`);

        console.log(userResponse.data.response[0]);
      });
    }
  }
}
</script>

<style scoped>
button {
  display: inline-block;
  background-color: #4d76a1;
  color: #fff;

  border-radius: 4px;
  text-decoration: none;
  font-family: 'Poppins', sans-serif;
  font-size: 12px;
  font-weight: 400;
  cursor: pointer;
  border: 1px solid #FAFAFA;

  padding: 4px 10px;
  margin-right: 30px;
}

button:hover {
  background-color: #3b5998;
}

</style>