<template>
  <div>
    <h1>Cart</h1>
    <div v-if="cartItems.length === 0">
      <p>Your cart is empty.</p>
    </div>
    <div v-else>
      <ul>
        <li v-for="item in groupedCartItems" :key="item.id">
          <img :src="item.product.image">
          <p>{{ item.product.name }}</p>
          <p>{{ item.product.price }}</p>
          <p>{{ item.quantity }}</p>
          <p>{{ item.totalPrice }}</p>
        </li>
      </ul>
      <p>{{ totalCost }}</p>
      <button @click="proceedToOrderPage">Place Order</button>
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

      axios
        .get('http://localhost:8000/api/cart/', { headers })
        .then((response) => {
          console.log(response.data);
          const cartItems = response.data;

          const groupedItems = {};

          cartItems.forEach((item) => {
            if (item.product in groupedItems) {
              groupedItems[item.product].quantity += item.quantity;
            } else {
              groupedItems[item.product] = {
                id: item.id,
                user: item.user,
                product: null,
                quantity: item.quantity,
              };
            }
          });

          const promises = [];

          Object.keys(groupedItems).forEach((productId) => {
            const promise = axios.get(`http://localhost:8000/api/products/${productId}/`, { headers });
            promises.push(promise);
          });

          Promise.all(promises)
            .then((responses) => {
              responses.forEach((response, index) => {
                const productId = Object.keys(groupedItems)[index];
                groupedItems[productId].product = response.data;
              });

              const cartItemsWithProduct = Object.values(groupedItems);

              cartItemsWithProduct.forEach((item) => {
                item.totalPrice = item.product.price * item.quantity;
              });

              this.cartItems = cartItemsWithProduct;
            })
            .catch((error) => {
              console.error('Failed to fetch product', error);
            });
        })
        .catch((error) => {
          console.error('Failed to fetch cart items', error);
        });
    },
    proceedToOrderPage() {
      const orderData = {
        orderItems: JSON.stringify(this.groupedCartItems),
        total_price: this.totalCost,
      };
      console.log(orderData)
      this.$router.push({ name: 'OrdersPage', query: orderData });
    },
  },
  computed: {
    groupedCartItems() {
      const groupedItems = {};

      this.cartItems.forEach((item) => {
        const productId = item.product.id;
        if (productId in groupedItems) {
          groupedItems[productId].quantity += item.quantity;
          groupedItems[productId].totalPrice += item.totalPrice;
        } else {
          groupedItems[productId] = {
            id: item.id,
            user: item.user,
            product: item.product,
            quantity: item.quantity,
            totalPrice: item.totalPrice,
          };
        }
      });

      return Object.values(groupedItems);
    },
    totalCost() {
      return this.groupedCartItems.reduce((total, item) => total + item.totalPrice, 0);
    },
  },
};
</script>
