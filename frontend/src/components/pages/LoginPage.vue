<template>
  <hea-der />
  <category-list />
  <login-form class="login-form" />
  <div class="reset-password">
    <a href="/reset-password">Сбросить пароль</a>
  </div>
  <div class="line"></div>
  <div class="text">
    Вы ещё не зарегистрированы?
  </div>
  <div class="link">
    <a href="/register" id="register-link">Зарегистрироваться</a>
  </div>
</template>

<script>
import LoginForm from "@/components/forms/LoginForm";
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";
export default {
  name: "LoginPage",
  components: {
    CategoryList,
    HeaDer,
    LoginForm
  }
}
</script>

<style scoped>
  .login-form {
    margin-bottom: 25px;
  }

  .text, link {
    font-family: "Poppins", sans-serif;
    font-weight: 500;
  }

  .text {
    margin: 15px 0 10px 0;
  }

  .line {
    border: none;
    border-top: 1px solid #000000;
    margin: 0 400px;
  }

  .reset-password {
    margin-bottom: 15px;
  }
</style>