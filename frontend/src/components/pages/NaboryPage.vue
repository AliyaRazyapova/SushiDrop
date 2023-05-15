<template>
  <div class="product-list">
    <div v-for="product in products" :key="product.id">
      <pro-duct :product-id="product.id" />
    </div>
  </div>
</template>
<script>
import ProDuct from "@/components/elements/ProDuct";

export default {
  name: 'NaboryPage',
  components: {
    ProDuct
  },
  data() {
    return {
      products: []
    }
  },
  mounted() {
    this.getProducts()
  },
  methods: {
    async getProducts() {
      try {
        const response = await fetch('http://localhost:8000/api/nabory/')
        const data = await response.json()
        this.products = data
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>