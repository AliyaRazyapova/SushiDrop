<template>
  <hea-der />
  <category-list />
  <div class="admin-discounts">
    <h2>Административная панель (скидки)</h2>
    <table class="discounts-table">
      <thead>
        <tr>
          <th>Продукт</th>
          <th>Процент скидки</th>
          <th>Начало</th>
          <th>Конец</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="discount in discounts" :key="discount.id">
          <td>{{ discount.product.name }}</td>
          <td>{{ formatDiscountPercentage(discount.discount_percentage) }}%</td>
          <td>{{ discount.start_date }}</td>
          <td>{{ discount.end_date }}</td>
          <td>
            <button @click="editDiscount(discount.id)" class="edit-button">Редактировать</button>
            <button @click="deleteDiscount(discount.id)" class="delete-button">Удалить</button>
          </td>
        </tr>
      </tbody>
    </table>
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
      discounts: []
    };
  },
  mounted() {
    this.getDiscounts();
  },
  methods: {
    formatDiscountPercentage(percentage) {
      return Math.round(percentage);
    },
    async getDiscounts() {
      try {
        const response = await axios.get('http://localhost:8000/api/discounts/list/');
        this.discounts = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    editDiscount(discountId) {
      this.$router.push(`/discounts/${discountId}/edit`);
    },
    deleteDiscount(discountId) {
      if (confirm('Вы уверены, что хотите удалить эту скидку?')) {
        const token = localStorage.getItem('access_token');
        axios.delete(`http://localhost:8000/api/discounts/${discountId}/`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
          .then(() => {
            alert('Discount deleted successfully!');
            this.getDiscounts();
          })
          .catch(error => {
            console.error(error);
            alert('Failed to delete discount');
          });
      }
    }
  }
};
</script>

<style scoped>
  .admin-discounts {
    margin-top: 80px;
  }

  .admin-discounts h2 {
    font-size: 28px;
    margin-bottom: 10px;
  }

  .discounts-table {
    width: 100%;
    border-collapse: collapse;
    margin: 50px;
  }

  .edit-button, .delete-button {
    padding: 5px 10px;
  }

  .edit-button {
    background-color: #0065b7;
    color: #fff;
    margin-right: 10px;
  }

  .delete-button {
    background-color: #F52341;
    color: #fff;
  }
</style>
