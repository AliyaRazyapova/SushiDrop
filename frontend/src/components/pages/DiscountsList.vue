<template>
  <div>
    <h1>Discounts</h1>
    <ul>
      <li v-for="discount in discounts" :key="discount.id">
        <p>Product: {{ discount.product.name }}</p>
        <p>Discount Percentage: {{ discount.discount_percentage }}</p>
        <p>Start Date: {{ discount.start_date }}</p>
        <p>End Date: {{ discount.end_date }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DiscountsList',
  data() {
    return {
      discounts: [],
    };
  },
  mounted() {
    this.getDiscounts();
  },
  methods: {
    getDiscounts() {
      axios.get('http://localhost:8000/api/discounts/list/')
        .then(response => {
          this.discounts = response.data;
        })
        .catch(error => {
          console.error('Failed to fetch discounts', error);
        });
    },
  },
};
</script>
