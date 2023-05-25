<template>
  <hea-der />
  <category-list />
  <div class="create-order-container">
    <h1 class="create-order-heading">Оформление заказа</h1>
    <div class="order-details-container">
      <h2 class="order-details-heading">Детали заказа</h2>
      <table class="order-details-table">
        <thead>
          <tr>
            <th>Продукт</th>
            <th>Цена</th>
            <th>Количество</th>
            <th>Общая стоимость</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in deserializedOrderItems" :key="item.id">
            <td>{{ item.product.name }}</td>
            <td>{{ item.product.price }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ item.totalPrice }}</td>
          </tr>
        </tbody>
      </table>
      <p class="total-price">Общая стоимость: {{ orderData.total_price }}</p>
    </div>
    <form @submit.prevent="createOrder" class="order-form">
      <div class="form-group">
        <label for="deliveryTime">Время доставки:</label>
        <input type="datetime-local" id="deliveryTime" v-model="orderData.delivery_time" required>
      </div>
      <div class="form-group">
        <label>Способ доставки:</label>
        <div class="row">
          <label>
            <input type="radio" value="self_pickup" v-model="orderData.delivery_method">
            Самовывоз
          </label>
          <label>
            <input type="radio" value="delivery" v-model="orderData.delivery_method">
            Доставка
          </label>
        </div>
      </div>
      <div v-if="orderData.delivery_method === 'delivery'" class="form-group">
        <label for="deliveryAddress">Адрес доставки:</label>
        <input type="text" id="deliveryAddress" v-model="orderData.delivery_address" required>
      </div>
      <div class="form-group">
        <label>Способ оплаты:</label>
        <div class="row">
          <label>
            <input type="radio" value="cash" v-model="orderData.payment_method">
            Наличные
          </label>
          <label>
            <input type="radio" value="card" v-model="orderData.payment_method">
            Карта
          </label>
        </div>
      </div>
      <button type="submit" class="create-order-button">Оформить заказ</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  components: {CategoryList, HeaDer},
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
      const orderItemsString = this.$route.query.orderItems;
      const orderItems = JSON.parse(orderItemsString);
      this.orderData.orderItems = orderItems;
      console.log(this.orderData);
    },
    createOrder() {
      const token = localStorage.getItem('access_token');
      const headers = {
        Authorization: `Bearer ${token}`,
      };

      const orderData = {
        delivery_time: this.orderData.delivery_time,
        delivery_method: this.orderData.delivery_method,
        delivery_address: this.orderData.delivery_address,
        payment_method: this.orderData.payment_method,
        order_items: this.orderData.orderItems,
      };

      axios
        .post('http://localhost:8000/api/orders/', orderData, { headers })
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

<style scoped>
  .create-order-container {
    background-color: #ffffff;
    color: #000000;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;

    margin-top: -50px;
  }

  .create-order-heading {
    text-align: center;
    font-size: 28px;
    margin-bottom: 20px;
  }

  .order-details-container {
    margin-bottom: 20px;
  }

  .order-details-heading {
    font-size: 20px;
    margin-bottom: 10px;
  }

  .order-details-table {
    width: 100%;
    border-collapse: collapse;
  }

  .order-details-table th,
  .order-details-table td {
    padding: 8px;
    text-align: center;
    border-bottom: 1px solid #000000;
  }

  .order-details-table th {
    background-color: #f0f0f0;
  }

  .total-price {
    font-weight: bold;
    margin-top: 10px;
    text-align: right;
  }

  .order-form {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .form-group {
    margin-bottom: 10px;
  }

  .form-group label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
  }

  .form-group input[type="text"],
  .form-group input[type="datetime-local"] {
    width: 100%;
    padding: 8px;
    border: 1px solid #000000;
    border-radius: 4px;
  }

  .create-order-button {
    font-weight: bold;
    font-size: 16px;
    padding: 12px 24px;
    background-color: #ff0000;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-top: 10px;
  }

  .create-order-button:hover {
    background-color: #cc0000;
  }

  .row {
    display: flex;
    flex-direction: row;
  }
</style>
