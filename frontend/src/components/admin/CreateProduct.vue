<template>
  <div>
    <form @submit.prevent="createProduct">
      <label>
        Категория:
        <select v-model="category">
          <option value="">Выберите категорию</option>
          <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
        </select>
      </label>
      <br>
      <label>
        Название:
        <input v-model="name" type="text">
      </label>
      <br>
      <label>
        Описание:
        <textarea v-model="description"></textarea>
      </label>
      <br>
      <label>
        Цена:
        <input v-model="price" type="number" step="0.01">
      </label>
      <br>
      <label>
        Изображение:
        <input @change="onImageChange" type="file">
      </label>
      <br>
      <label>
        Граммы:
        <input v-model="gramms" type="number">
      </label>
      <br>
      <button type="submit">Создать продукт</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'CreateProduct',
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
