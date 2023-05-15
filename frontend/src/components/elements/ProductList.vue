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
  name: 'ProductList',
  components: {
    ProDuct
  },
  props: {
    apiUrl: {
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
    this.getProducts()
  },
  methods: {
    async getProducts() {
      try {
        const response = await fetch(this.URL)
        const data = await response.json()
        this.products = data
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
