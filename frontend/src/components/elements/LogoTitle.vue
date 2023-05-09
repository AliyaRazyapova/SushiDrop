<template>
  <div class="container">
    <div class="logo">
      <svg width="200" height="60" viewBox="0 0 250 60" xmlns="http://www.w3.org/2000/svg">
        <text x="60" y="40" font-family="Helvetica, Arial, sans-serif" font-size="36" fill="#333333">Sushi</text>
        <text x="133" y="40" font-family="Helvetica, Arial, sans-serif" font-size="36" fill="#FFD700">Drop</text>
        <path d="M70 10 C 70 15, 75 20, 80 20 C 85 20, 90 15, 90 10 C 90 5, 85 0, 80 0 C 75 0, 70 5, 70 10 Z" fill="#FFD700"/>
        <circle cx="85" cy="15" r="4" fill="#333333"/>
        <path d="M105 25 C 105 30, 110 35, 115 35 C 120 35, 125 30, 125 25 C 125 20, 120 15, 115 15 C 110 15, 105 20, 105 25 Z" fill="#FFD700"/>
        <circle cx="120" cy="30" r="4" fill="#333333"/>
        <path d="M150 10 C 150 15, 155 20, 160 20 C 165 20, 170 15, 170 10 C 170 5, 165 0, 160 0 C 155 0, 150 5, 150 10 Z" fill="#FFD700"/>
        <circle cx="165" cy="15" r="4" fill="#333333"/>
      </svg>
    </div>
    <div class="title">
      Доставка суши и роллов
    </div>
  </div>
</template>

<script>
export default {
  name: "LogoTitle"
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
}

.logo {
  width: 168px;
  height: 51px;
}

.title {
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: 600;
  font-size: 30px;
  line-height: 45px;
  color: #2F2F2F;

  text-align: center;
  padding: 10px 134px;
}
</style>