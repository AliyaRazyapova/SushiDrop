<template>
  <div>
    <h1>Create Discount</h1>
    <form @submit.prevent="createDiscount">
      <label for="product">Product:</label>
      <select v-model="selectedProduct" id="product">
        <option v-for="product in products" :value="product.id" :key="product.id">{{ product.name }}</option>
      </select>
      <label for="discountPercentage">Discount Percentage:</label>
      <input type="number" v-model="discountPercentage" id="discountPercentage">
      <label for="startDate">Start Date:</label>
      <input type="date" v-model="startDate" id="startDate">
      <label for="endDate">End Date:</label>
      <input type="date" v-model="endDate" id="endDate">
      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CreateDiscount',
  data() {
    return {
      selectedProduct: null,
      discountPercentage: null,
      startDate: null,
      endDate: null,
      products: [], // Populate this with available products
    };
  },
  mounted() {
    this.getProducts();
  },
  methods: {
    getProducts() {
      axios.get('http://localhost:8000/api/products/')
        .then(response => {
          console.log(response.data);
          this.products = response.data;
        })
        .catch(error => {
          console.error('Failed to fetch products', error);
        });
    },
    createDiscount() {
      const payload = {
        product: this.selectedProduct,
        discount_percentage: this.discountPercentage,
        start_date: this.startDate,
        end_date: this.endDate,
      };

      console.log(payload)

      const token = localStorage.getItem('access_token');
      const headers = {
        Authorization: `Bearer ${token}`,
      };

      axios.post('http://localhost:8000/api/discounts/add/', payload, {
        headers: headers,
      })
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error('Failed to create discount', error);
        });
    },
  },
};
</script>
