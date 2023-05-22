<template>
  <div>
    <h1>Create Order</h1>
    <div>
      <h2>Order Details</h2>
      <ul>
        <li v-for="item in deserializedOrderItems" :key="item.id">
          <p>{{ item.product.name }}</p>
          <p>{{ item.product.price }}</p>
          <p>{{ item.quantity }}</p>
          <p>{{ item.totalPrice }}</p>
        </li>
      </ul>
      <p>Total Price: {{ orderData.total_price }}</p>
    </div>
    <form @submit.prevent="createOrder">
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
        orderItems: [],
        total_price: 0,
        delivery_time: '',
        delivery_method: 'self_pickup',
        delivery_address: '',
        payment_method: 'cash',
      },
    };
  },
  mounted() {
    this.getOrderDataFromCart();
  },
  computed: {
    deserializedOrderItems() {
      const orderItemsString = this.$route.query.orderItems;
      const orderItems = JSON.parse(orderItemsString);
      return orderItems;
    },
  },
  methods: {
    getOrderDataFromCart() {
      this.orderData = this.$route.query;
      console.log(this.orderData)
    },
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