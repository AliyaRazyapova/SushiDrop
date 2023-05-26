<template>
  <hea-der />
  <category-list />
  <div class="create-product">
    <h1>Создание продукта</h1>
    <form @submit.prevent="createProduct" class="product-form">
      <label>
        Категория:
        <select v-model="category" class="form-select">
          <option value="">Выберите категорию</option>
          <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
        </select>
      </label>
      <br>
      <label>
        Название:
        <input v-model="name" type="text" class="form-input">
      </label>
      <br>
      <label>
        Описание:
        <textarea v-model="description" class="form-textarea"></textarea>
      </label>
      <br>
      <label>
        Цена:
        <input v-model="price" type="number" step="0.01" class="form-input">
      </label>
      <br>
      <label>
        Изображение:
        <input @change="onImageChange" type="file" class="form-file">
      </label>
      <br>
      <label>
        Граммы:
        <input v-model="gramms" type="number" class="form-input">
      </label>
      <br>
      <button type="submit" class="form-button">Создать продукт</button>
    </form>
  </div>
</template>

<script>
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  name: 'CreateProduct',
  components: {CategoryList, HeaDer},
  data() {
    return {
      category: '',
      name: '',
      description: '',
      price: 0,
      gramms: 0,
      image: null,
      categories: [],
    }
  },
  created() {
    this.loadCategories()
  },
  methods: {
    async loadCategories() {
      try {
        const response = await fetch('http://localhost:8000/api/products/categories/')
        const data = await response.json()
        this.categories = data
      } catch (error) {
        console.log('Failed to load categories:', error)
      }
    },
    onImageChange(event) {
      this.image = event.target.files[0]
    },
    async createProduct() {
      try {
        const formData = new FormData()
        formData.append('category_id', this.category)
        formData.append('name', this.name)
        formData.append('description', this.description)
        formData.append('price', this.price)
        formData.append('gramms', this.gramms)
        formData.append('image', this.image)

        const response = await fetch('http://localhost:8000/api/products/create/', {
          method: 'POST',
          body: formData,
        })

        const data = await response.json()
        if (data.success) {
          alert('Продукт успешно создан!')
          this.$router.push('/')
        } else {
          alert('Не удалось создать продукт: ' + data.message)
        }
      } catch (error) {
        console.log('Failed to create product:', error)
      }
    },
  },
}
</script>

<style>
  .create-product {
    max-width: 400px;
    margin: 0 auto;
  }

  .product-form {
    display: flex;
    flex-direction: column;
  }

  label {
    margin-top: 10px;
  }

  .form-select,
  .form-input,
  .form-textarea,
  .form-file {
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
