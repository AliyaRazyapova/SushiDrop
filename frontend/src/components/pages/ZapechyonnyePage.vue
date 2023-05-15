<template>
  <hea-der />
  <category-list />
  <div class="main">
    <div class="title">
      Запечённые
    </div>
  </div>
  <div class="product-list">
    <product-list-page URL="http://localhost:8000/api/products/zapechyonnye/" />
  </div>
</template>

<script>
import ProductListPage from "@/components/elements/ProductList";
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  name: 'ZapechyonnyePage',
  components: {
    CategoryList,
    HeaDer,
    ProductListPage
  }
}
</script>
