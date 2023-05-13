<template>
  <hea-der></hea-der>
  <category-list></category-list>
  <div className="main">
    <div className="title">
      Запечённые
    </div>
  </div>
</template>

<script>
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  name: "GoryacheeISalatyPage",
  components: {CategoryList, HeaDer}
}
</script>

<style scoped>
.main {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80px;
}

.title {
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 24px;
  line-height: 36px;
  color: #212121;

  margin: auto;
}
</style>