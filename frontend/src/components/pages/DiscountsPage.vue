<template>
  <hea-der />
  <category-list />
  <discounts-list />
</template>

<script>
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";
import DiscountsList from "@/components/pages/DiscountsList";
export default {
  name: "DiscountsPage",
  components: {DiscountsList, CategoryList, HeaDer}
}
</script>

<style scoped>

</style>