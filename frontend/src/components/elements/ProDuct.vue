<template>
  <div class="product">
    <img :src="product.image" alt="product image">
    <div class="name">{{ product.name }}</div>
    <div class="gramms_price">
      <div class="gramms">{{product.gramms}} гр.</div>
      <div class="price_1">
        <div class="price">{{ product.price }} ₽</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProDuct',
  props: {
    productId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      product: {}
    }
  },
  mounted() {
    this.getProduct(this.productId)
  },
  methods: {
    async getProduct(productId) {
      try {
        const response = await fetch(`http://localhost:8000/api/products/${productId}/`)
        const data = await response.json()
        this.product = data
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>

<style>
  .product {
    width: 250px;
    height: 270px;
  }

  img {
    width: 250px;
    height: 184px;
  }

  .name {
    font-family: 'PT Sans', sans-serif;
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 21px;

    color: #000000;

    margin-left: 15px;
  }

  .gramms_price {
    display: flex;
    flex-direction: row;
  }

  .gramms {
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 11.3208px;
    line-height: 17px;

    color: #7C909C;

    margin: 16px 0 0 15px;
  }

  .price_1 {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: right;

    margin: 15px 15px 0 auto;

    width: 93.93px;
    height: 27.27px;

    border: 1.5px solid #F52341;
    border-radius: 3.78742px;
  }

  .price {
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 13.6347px;
    line-height: 20px;
    color: #F52341;
  }
</style>