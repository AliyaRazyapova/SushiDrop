<template>
  <hea-der />
  <registration-form />
</template>

<script>
import HeaDer from "@/components/elements/HeaDer";
import RegistrationForm from "@/components/forms/RegistrationForm";

export default {
  name: "RegistrationPage",
  components: {
    RegistrationForm,
    HeaDer
  }
}
</script>

<style scoped>

</style>