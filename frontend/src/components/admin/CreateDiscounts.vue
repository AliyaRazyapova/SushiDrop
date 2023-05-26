<template>
  <hea-der />
  <category-list />
  <div class="create-discount">
    <h1>Создание cкидки</h1>
    <form @submit.prevent="createDiscount" class="discount-form">
      <label for="product">Продукт</label>
      <select v-model="selectedProduct" id="product" class="form-select">
        <option v-for="product in products" :value="product.id" :key="product.id">{{ product.name }}</option>
      </select>
      <label for="discountPercentage">Процент скидки</label>
      <input type="number" v-model="discountPercentage" id="discountPercentage" class="form-input">
      <label for="startDate">Начало</label>
      <input type="date" v-model="startDate" id="startDate" class="form-input">
      <label for="endDate">Конец</label>
      <input type="date" v-model="endDate" id="endDate" class="form-input">
      <button type="submit" class="form-button">Создать</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  name: 'CreateDiscount',
  components: {CategoryList, HeaDer},
  data() {
    return {
      selectedProduct: null,
      discountPercentage: null,
      startDate: null,
      endDate: null,
      products: [],
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

<style>
  .create-discount {
    max-width: 400px;
    margin: 80px auto;
  }

  .discount-form {
    display: flex;
    flex-direction: column;
  }

  label {
    margin-top: 10px;
  }

  .form-select,
  .form-input {
    padding: 8px;
    margin-top: 5px;
  }

  .form-button {
    padding: 10px 20px;
    margin-top: 10px;
    background-color: #F52341;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
</style>
