<template>
  <hea-der />
  <category-list />
  <v-k-form />
</template>

<script>
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";
import VKForm from "@/components/forms/VKForm";

export default {
  name: "VKPage",
  components: {VKForm, CategoryList, HeaDer}
}
</script>

<style scoped>

</style>