<template>
  <hea-der />
  <category-list />
  <div class="main">
    <div class="title">
      SushiDrop
    </div>
  </div>
  <div class="product-list">
    <product-list URL="http://localhost:8000/api/products/" />
  </div>
</template>

<script>
import '@/assets/pages.css';
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";
import ProductList from "@/components/elements/ProductList";

export default {
  name: "MainPage",
  components: {
    ProductList,
    CategoryList,
    HeaDer
  }
}
</script>
