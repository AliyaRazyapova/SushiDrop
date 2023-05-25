<template>
  <div>
    <div class="search-bar">
      <input class="search-bar-input" type="text" v-model="searchQuery" placeholder="Введите название..." @input="searchProducts" />
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
    margin: 1px 19px 17px 19px;
    width: 1100px;
    height: 26px;
  }

  .search-bar-input {
    margin: 1px 19px 17px 19px;
    padding-left: 10px;

    width: 1100px;
    height: 27px;

    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    outline: none;
  }

  .product-list {
    display: flex;
    flex-wrap: wrap;
  }
</style>
