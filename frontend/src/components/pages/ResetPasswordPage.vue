<template>
  <hea-der />
  <category-list />
  <reset-password />
</template>

<script>
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";
import ResetPassword from "@/components/forms/ResetPassword";

export default {
  name: "ResetPasswordPage",
  components: {ResetPassword, CategoryList, HeaDer}
}
</script>

<style scoped>

</style>