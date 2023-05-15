<template>
  <div>
    <form @submit.prevent="createProduct">
      <label>
        Category:
        <select v-model="category">
          <option value="">Выберите категорию</option>
          <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
        </select>
      </label>
      <br>
      <label>
        Name:
        <input v-model="name" type="text">
      </label>
      <br>
      <label>
        Description:
        <textarea v-model="description"></textarea>
      </label>
      <br>
      <label>
        Price:
        <input v-model="price" type="number" step="0.01">
      </label>
      <br>
      <label>
        Image:
        <input @change="onImageChange" type="file">
      </label>
      <br>
      <label>
        Gramms
        <input v-model="gramms" type="number">
      </label>
      <br>
      <button type="submit">Create Product</button>
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
      const response = await fetch('http://localhost:8000/api/categories/')
      const data = await response.json()
      this.categories = data
    },
    onImageChange(event) {
      this.image = event.target.files[0]
    },
    async createProduct() {
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
        alert('Product created successfully!')
        this.category = ''
        this.name = ''
        this.description = ''
        this.price = 0
        this.gramms = 0
        this.image = null
      } else {
      alert('Failed to create product: ' + data.message)
      }
    },
  },
}
</script>