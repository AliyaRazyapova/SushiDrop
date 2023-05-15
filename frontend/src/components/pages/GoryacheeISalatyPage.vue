<template>
  <hea-der />
  <category-list />
  <div class="main">
    <div class="title">
      Горячее и салаты
    </div>
  </div>
  <div class="product-list">
    <product-list-page URL="http://localhost:8000/api/products/goryachee-i-salaty/" />
  </div>
</template>

<script>
import '@/assets/pages.css';
import ProductListPage from "@/components/elements/ProductList";
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  name: 'GoryacheeISalatyPage',
  components: {
    CategoryList,
    HeaDer,
    ProductListPage
  }
}
</script>
