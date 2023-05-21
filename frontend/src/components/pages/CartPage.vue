<template>
  <div>
    <h1>Cart</h1>
    <div v-if="cartItems.length === 0">
      <p>Your cart is empty.</p>
    </div>
    <div v-else>
      <ul>
        <li v-for="item in cartItems" :key="item.id">
          <p>Product: {{ item.product }}</p>
          <p>Quantity: {{ item.quantity }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cartItems: [],
    };
  },
  mounted() {
    this.getCartItems();
  },
  methods: {
    getCartItems() {
      const token = localStorage.getItem('access_token');
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      console.log(headers)

      axios
        .get('http://localhost:8000/api/cart/', { headers })
        .then((response) => {
          this.cartItems = response.data;
        })
        .catch((error) => {
          console.error('Failed to fetch cart items', error);
        });
    },
  },
};
</script>