<template>
  <nav>
    <ul>
      <li :class="{ 'active': activeTab === 0 }"><a href="/">Главная</a></li>
      <li :class="{ 'active': activeTab === 1 }"><a href="/nabory">Наборы</a></li>
      <li :class="{ 'active': activeTab === 2 }"><a href="/premium">Премиум</a></li>
      <li :class="{ 'active': activeTab === 3 }"><a href="/rolly-i-sushi">Роллы и суши</a></li>
      <li :class="{ 'active': activeTab === 4 }"><a href="/tempura">Темпура</a></li>
      <li :class="{ 'active': activeTab === 5 }"><a href="/zapechyonnye">Запечённые</a></li>
      <li :class="{ 'active': activeTab === 6 }"><a href="/goryachee-i-salaty">Горячее и салаты</a></li>
      <li :class="{ 'active': activeTab === 7 }"><a href="/sousy">Соусы</a></li>
      <li :class="{ 'active': activeTab === 8 }"><a href="/napitki-i-deserty">Напитки и десерты</a></li>
      <li :class="{ 'active': activeTab === 9 }"><a href="/spetsii">Специи</a></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'CategoryList',
  data() {
    return {
      activeTab: 0,
    };
  },
  created() {
    this.activeTab = this.getActiveTab();
  },
  methods: {
    getActiveTab() {
      const path = window.location.pathname;
      switch (path) {
        case '/nabory':
          return 1;
        case '/premium':
          return 2;
        case '/rolly-i-sushi':
          return 3;
        case '/tempura':
          return 4;
        case '/zapechyonnye':
          return 5;
        case '/goryachee-i-salaty':
          return 6;
        case '/sousy':
          return 7;
        case '/napitki-i-deserty':
          return 8;
        case '/spetsii':
          return 9;
        default:
          return 0;
      }
    },
  },
};
</script>

<style>
  nav {
    display: flex;
    justify-content: center;
  }

  ul {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
  }

  li {
    margin: 0 1rem;
  }

  li a {
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 500;
    line-height: 18px;
    color: #464646;
    text-decoration: none;
    position: relative;
  }

  li.active a:before {
    content: "";
    position: absolute;
    left: 0;
    bottom: -3px;
    width: 100%;
    height: 2px;
    background-color: #F52341;
  }

  li.active a {
    font-weight: 700;
    color: #F52341;
  }
</style>
