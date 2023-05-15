<template>
  <hea-der />
  <category-list />
  <div class="main">
    <div class="title">
      Специи
    </div>
  </div>
  <div class="product-list">
    <product-list-page URL="http://localhost:8000/api/products/spetsii/" />
  </div>
</template>

<script>
import ProductListPage from "@/components/elements/ProductList";
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  name: 'SpetsiiPage',
  components: {
    CategoryList,
    HeaDer,
    ProductListPage
  }
}
</script>
