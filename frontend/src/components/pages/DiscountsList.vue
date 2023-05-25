<template>
  <div class="discounts-container">
    <h1 class="discounts-title">Скидки</h1>
    <ul class="discounts-list">
      <li v-for="discount in discounts" :key="discount.id" class="discount-item">
        <div class="discount-image">
          <img :src="discount.product.image" alt="Изображение товара" />
        </div>
        <div class="discount-details">
          <p class="discount-product">Товар: {{ discount.product.name }}</p>
          <p class="discount-percentage">Процент скидки: {{ formatDiscountPercentage(discount.discount_percentage) }}%</p>
          <p class="discount-start">Начало: {{ discount.start_date }}</p>
          <p class="discount-end">Конец: {{ discount.end_date }}</p>
          <p class="price">Цена: {{ discount.product.price }}₽</p>
          <p class="discount-price">Скидочная цена: {{ calculateDiscountedPrice(discount) }}₽</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<style>
.discount-image {
  height: 100px;
  margin-bottom: 10px;
}

.discount-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.discounts-container {
  background-color: #FFFFFF;
  padding: 20px;
}

.discounts-title {
  color: #000000;
  font-size: 24px;
  margin-bottom: 10px;
}

.discounts-list {
  list-style-type: none;
  padding: 0;
}

.discount-item {
  margin-bottom: 20px;
  padding: 10px;
}

.discount-product {
  color: #000000;
  font-weight: bold;
}

.discount-percentage, .discount-price {
  color: #F52341;
}

.discount-start,
.discount-end, .price {
  color: #000000;
}
</style>

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
    formatDiscountPercentage(percentage) {
      return Math.round(percentage);
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
