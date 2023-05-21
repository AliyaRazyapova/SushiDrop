<template>
  <div>
    <h1>Create Order</h1>
    <form @submit.prevent="createOrder">
      <div>
        <label for="totalPrice">Total Price:</label>
        <input type="number" id="totalPrice" v-model="orderData.total_price" required>
      </div>
      <div>
        <label for="deliveryTime">Delivery Time:</label>
        <input type="datetime-local" id="deliveryTime" v-model="orderData.delivery_time" required>
      </div>
      <div>
        <label for="deliveryMethod">Delivery Method:</label>
        <input type="text" id="deliveryMethod" v-model="orderData.delivery_method" required>
      </div>
      <div>
        <label for="paymentMethod">Payment Method:</label>
        <input type="text" id="paymentMethod" v-model="orderData.payment_method" required>
      </div>
      <div>
        <label for="deliveryAddress">Delivery Address:</label>
        <input type="text" id="deliveryAddress" v-model="orderData.delivery_address" required>
      </div>
      <button type="submit">Create Order</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'OrdersPage',
  data() {
    return {
      orderData: {
        total_price: 0,
        delivery_time: '',
        delivery_method: '',
        payment_method: '',
        delivery_address: '',
      },
    };
  },
  methods: {
    createOrder() {
      const token = localStorage.getItem('access_token');
      const headers = {
        Authorization: `Bearer ${token}`,
      };

      axios
        .post('http://localhost:8000/api/orders/', this.orderData, { headers })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.error('Failed to create order', error);
        });
    },
  },
};
</script>
