<template>
  <hea-der />
  <category-list />
  <div class="main">
    <div class="title">
      Соусы
    </div>
  </div>
  <div class="product-list">
    <product-list-page URL="http://localhost:8000/api/products/sousy/" />
  </div>
</template>

<script>
import '@/assets/pages.css';
import ProductListPage from "@/components/elements/ProductList";
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  name: 'SousyPage',
  components: {
    CategoryList,
    HeaDer,
    ProductListPage
  }
}
</script>
