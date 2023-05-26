<template>
  <hea-der />
  <category-list />
  <h2>Редактирование продукта</h2>
  <form @submit.prevent="updateProduct" class="product-form">
    <label htmlFor="name">Название</label>
    <input v-model="product.name" type="text" id="name" required>

    <label htmlFor="description">Описание</label>
    <textarea v-model="product.description" id="description" required></textarea>

    <label htmlFor="gramms">Граммы</label>
    <input v-model="product.gramms" type="number" id="gramms" required>

    <label htmlFor="price">Цена</label>
    <input v-model="product.price" type="number" step="0.01" id="price" required>

    <label htmlFor="image">Изображение</label>
    <input type="file" id="image" accept="image/*" @change="handleImageUpload">

    <button type="submit" className="btn-update">Обновить продукт</button>
  </form>
</template>

<script>
import axios from 'axios';
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  components: {CategoryList, HeaDer},
  data() {
    return {
      product: {
        name: '',
        description: '',
        gramms: '',
        price: '',
        image: null,
      },
    };
  },
  mounted() {
    const productId = this.$route.params.productId;
    this.fetchProduct(productId);
  },
  methods: {
    fetchProduct(productId) {
      axios.get(`http://localhost:8000/api/products/${productId}/`)
          .then(response => {
            this.product = response.data;
          })
          .catch(error => {
            console.error('Не удалось загрузить продукт', error);
          });
    },
    updateProduct() {
      const productId = this.$route.params.productId;
      const formData = new FormData();
      formData.append('name', this.product.name);
      formData.append('description', this.product.description);
      formData.append('gramms', this.product.gramms);
      formData.append('price', this.product.price);
      formData.append('image', this.product.image);

      axios.post(`http://localhost:8000/api/products/${productId}/edit/`, formData)
          .then(response => {
            if (response.data.success) {
              alert('Продукт успешно обновлен!');
            } else {
              alert('Не удалось обновить продукт: ' + response.data.message);
            }
          })
          .catch(error => {
            console.error('Не удалось обновить продукт', error);
          });
    },
    handleImageUpload(event) {
      const file = event.target.files[0];
      this.product.image = file;
    },
  },
};
</script>

<style scoped>
  .product-form {
    max-width: 400px;
    margin: 0 auto;
  }

  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    margin-top: 15px;
  }

  input[type="text"],
  textarea,
  input[type="number"] {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
  }

  button {
    padding: 8px 16px;
    background-color: #F52341;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin: 20px 0 0 0;
  }

  h2 {
    margin: 40px;
  }
</style>
