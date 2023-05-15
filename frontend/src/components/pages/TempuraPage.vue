<template>
  <hea-der />
  <category-list />
  <div class="main">
    <div class="title">
      Темпура
    </div>
  </div>
  <div class="product-list">
    <product-list-page URL="http://localhost:8000/api/products/rolly-i-sushi/" />
  </div>
</template>

<script>
import ProductListPage from "@/components/elements/ProductList";
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  name: 'TempuraPage',
  components: {
    CategoryList,
    HeaDer,
    ProductListPage
  }
}
</script>
