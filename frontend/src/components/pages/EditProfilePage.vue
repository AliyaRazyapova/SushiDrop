<template>
  <hea-der />
  <category-list />
  <edit-profile />
</template>

<script>
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";
import EditProfile from "@/components/elements/EditProfile";
export default {
  name: "EditProfilePage",
  components: {EditProfile, CategoryList, HeaDer}
}
</script>

<style scoped>

</style>