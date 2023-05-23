<template>
  <div>
    <div class="search-bar">
      <input type="text" v-model="searchQuery" placeholder="Search..." @input="searchProducts" />
    </div>
    <div class="product-list">
      <div v-for="product in filteredProducts" :key="product.id">
        <product-profile :productId="product.id" @goToProfile="goToProfile" />
      </div>
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
      products: [],
      searchQuery: ''
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
      this.$router.push({ name: 'ProductProfile', params: { productId } });
    },
    searchProducts() {
      const searchRegex = new RegExp(this.searchQuery, 'i');
      this.filteredProducts = this.products.filter(product => searchRegex.test(product.name));
    }
  },
  computed: {
    filteredProducts() {
      if (this.searchQuery === '') {
        return this.products;
      } else {
        const searchRegex = new RegExp(this.searchQuery, 'i');
        return this.products.filter(product => searchRegex.test(product.name));
      }
    }
  }
}
</script>

<style scoped>
  .search-bar {
    margin-bottom: 1rem;
  }

  .product-list {
    display: flex;
    flex-wrap: wrap;
  }
</style>
