<template>
  <div class="header">
    <logo-title />
    <header-buttons />
  </div>
</template>

<script>
import HeaderButtons from "@/components/elements/HeaderButtons";
import LogoTitle from "@/components/elements/LogoTitle";

export default {
name: "HeaDer",
  components: {LogoTitle, HeaderButtons}
}
</script>

<style scoped>
.header {
  display: flex;
  flex-direction: row;
}
</style>