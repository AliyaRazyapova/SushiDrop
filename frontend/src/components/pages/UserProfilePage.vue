<template>
  <hea-der />
  <category-list />
  <user-profile />
</template>

<script>
import UserProfile from "@/components/elements/UserProfile";
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  name: "UserProfilePage",
  components: {CategoryList, HeaDer, UserProfile}
}
</script>