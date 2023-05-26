<template>
  <div>
    <h2>Edit Discount</h2>
    <form @submit.prevent="updateDiscount">
      <label for="product">Product:</label>
      <select id="product" v-model="discount.product" :key="'product'">
        <option v-for="product in products" :key="product.id" :value="product.id">{{ product.name }}</option>
      </select>

      <label for="discountPercentage">Discount Percentage:</label>
      <input type="number" id="discountPercentage" v-model="discount.discountPercentage" :key="'discountPercentage'">

      <label for="startDate">Start Date:</label>
      <input type="date" id="startDate" v-model="discount.startDate" :key="'startDate'">

      <label for="endDate">End Date:</label>
      <input type="date" id="endDate" v-model="discount.endDate" :key="'endDate'">

      <button type="submit">Update Discount</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      discountId: null,
      discount: {
        product: null,
        discountPercentage: null,
        startDate: null,
        endDate: null
      },
      products: []
    };
  },
  mounted() {
    this.discountId = this.$route.params.discountId;
    this.getDiscount();
    this.getProducts();
  },
  methods: {
    async getDiscount() {
      try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get(`http://localhost:8000/api/discounts/${this.discountId}/`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.discount = response.data;
      } catch (error) {
        console.error('Failed to fetch discount', error);
      }
    },
    async getProducts() {
      try {
        const response = await axios.get(`http://localhost:8000/api/products/`);
        this.products = response.data;
      } catch (error) {
        console.error('Failed to fetch products', error);
      }
    },
    async updateDiscount() {
      try {
        await axios.put(`http://localhost:8000/api/discounts/${this.discountId}/`, this.discount);
        alert('Discount updated successfully!');
      } catch (error) {
        console.error('Failed to update discount', error);
        alert('Failed to update discount');
      }
    }
  }
};
</script>
