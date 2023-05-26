<template>
  <hea-der />
  <category-list />
  <div class="admin-panel">
    <h2>Административная панель</h2>
    <div class="buttons">
      <button class="menu-button" @click="AddProduct">Добавление продуктов</button>
      <button class="menu-button" @click="AddDiscount">Добавление скидок</button>
      <button class="menu-button" @click="Discounts">Скидки</button>
    </div>
  </div>
</template>

<script>
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  components: {
    CategoryList,
    HeaDer
  },
  methods: {
    AddProduct() {
      this.$router.push('/products/create');
    },
    AddDiscount() {
      this.$router.push('/discounts/add');
    },
    Discounts() {
      this.$router.push('/admin/discounts');
    }
  }
}
</script>

<style scoped>
  .admin-panel {
    margin: 40px;
  }

  .buttons {
    display: flex;
    justify-content: center;
    margin: 40px;
  }

  .menu-button {
    padding: 10px 20px;
    margin: 0 10px;
    background-color: #F52341;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }

  .component {
    margin-bottom: 20px;
  }
</style>