<template>
  <div class="product">
    <h2>{{ product.name }}</h2>
    <img :src="product.image" alt="product image">
    <p>{{ product.description }}</p>
    <p>{{ product.price }}</p>
  </div>
</template>

<script>
export default {
  name: 'ProDuct',
  props: {
    productId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      product: {}
    }
  },
  mounted() {
    this.getProduct(this.productId)
  },
  methods: {
    async getProduct(productId) {
      try {
        const response = await fetch(`http://localhost:8000/api/products/${productId}/`)
        const data = await response.json()
        this.product = data
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
