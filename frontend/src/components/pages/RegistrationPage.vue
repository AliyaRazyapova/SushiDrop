<template>
  <hea-der />
  <category-list />
  <registration-form />
</template>

<script>
import HeaDer from "@/components/elements/HeaDer";
import RegistrationForm from "@/components/forms/RegistrationForm";
import CategoryList from "@/components/elements/CategoryList";

export default {
  name: "RegistrationPage",
  components: {
    CategoryList,
    RegistrationForm,
    HeaDer
  }
}
</script>

<style scoped>

</style>