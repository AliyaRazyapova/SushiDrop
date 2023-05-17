<template>
  <hea-der />
  <category-list />
  <product-profile />
</template>

<script>
import ProductProfile from "@/components/elements/ProductProfile";
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  name: "ProductPage",
  components: {
    CategoryList,
    HeaDer,
    ProductProfile
  }
}
</script>

<style scoped>

</style>