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
        <label>Delivery Method:</label>
        <label>
          <input type="radio" value="self_pickup" v-model="orderData.delivery_method">
          Self Pickup
        </label>
        <label>
          <input type="radio" value="delivery" v-model="orderData.delivery_method">
          Delivery
        </label>
      </div>
      <div v-if="orderData.delivery_method === 'delivery'">
        <label for="deliveryAddress">Delivery Address:</label>
        <input type="text" id="deliveryAddress" v-model="orderData.delivery_address" required>
      </div>
      <div>
        <label>Payment Method:</label>
        <label>
          <input type="radio" value="cash" v-model="orderData.payment_method">
          Cash
        </label>
        <label>
          <input type="radio" value="card" v-model="orderData.payment_method">
          Card
        </label>
      </div>
      <button type="submit">Create Order</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      orderData: {
        total_price: 0,
        delivery_time: '',
        delivery_method: 'self_pickup',
        delivery_address: '',
        payment_method: 'cash',
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