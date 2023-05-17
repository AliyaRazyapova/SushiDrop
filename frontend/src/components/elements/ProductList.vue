<template>
  <div class="product-list">
    <div v-for="product in products" :key="product.id">
      <product-profile :productId="product.id" @goToProfile="goToProfile" />
    </div>
  </div>
</template>

<script>
import ProductProfile from "@/components/elements/ProductProfile";

export default {
  name: 'ProductList',
  components: {
    ProductProfile
  },
  props: {
    URL: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      products: []
    }
  },
  mounted() {
    this.getProducts();
  },
  methods: {
    async getProducts() {
      try {
        const response = await fetch(this.URL);
        const data = await response.json();
        this.products = data;
      } catch (error) {
        console.error(error);
      }
    },
    goToProfile(productId) {
      console.log(productId)
      this.$router.push({ name: 'ProductProfile', params: { productId } });
    }
  }
}
</script>

<style scoped>
  .product-list {
    flex-wrap: wrap;
  }
</style>
