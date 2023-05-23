<template>
  <div>
    <h1>Discounts</h1>
    <ul>
      <li v-for="discount in discounts" :key="discount.id">
        <p>Product: {{ discount.product.name }}</p>
        <p>Discount Percentage: {{ discount.discount_percentage }}</p>
        <p>Price: {{ discount.product.price }}</p>
        <p>Discounted Price: {{ calculateDiscountedPrice(discount) }}</p>
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
      axios.get('http://localhost:8000/api/discounts/')
        .then(response => {
          console.log(response.data);
          this.discounts = response.data;
        })
        .catch(error => {
          console.error('Failed to fetch discounts', error);
        });
    },
    calculateDiscountedPrice(discount) {
      const originalPrice = discount.product.price;
      const discountPercentage = discount.discount_percentage;
      const discountedPrice = originalPrice * (1 - discountPercentage / 100);
      return discountedPrice.toFixed(2);
    },
  },
};
</script>