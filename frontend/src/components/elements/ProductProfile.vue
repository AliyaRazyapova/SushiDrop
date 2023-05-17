<template>
    <div :class="{'product': true, 'product--profile': isProfileUrl}" @click="navigateToProfile">
      <img :src="product.image" alt="product image">
      <div :class="{'name': true, 'name--profile': isProfileUrl}">{{ product.name }}</div>
      <div :class="{'gramms_price': true, 'gramms_price--profile': isProfileUrl}">
        <div :class="{'gramms': true, 'gramms--profile': isProfileUrl}">{{ product.gramms }} гр.</div>
        <div :class="{'price_1': true, 'price_1--profile': isProfileUrl}">
          <div :class="{'price': true, 'price--profile': isProfileUrl}">{{ product.price }} ₽</div>
        </div>
      </div>
      <div :class="{'description': false, 'description': isProfileUrl}">{{product.description}}</div>
  </div>
</template>

<script>
export default {
  name: 'ProductProfile',
  props: {
    productId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      product: {},
      isProfileUrl: false
    }
  },
  mounted() {
    this.getProduct();
    this.checkUrl();
  },
  methods: {
    async getProduct() {
      try {
        const response = await fetch(`http://localhost:8000/api/products/${this.productId}/`);
        if (!response.ok) {
          throw new Error(response.status + ' ' + response.statusText);
        }
        const data = await response.json();
        this.product = data;
      } catch (error) {
        console.error(error);
      }
    },
    checkUrl() {
      this.isProfileUrl = this.$route.name === 'ProductProfile' && this.$route.params.productId == this.productId;
    },
    navigateToProfile() {
      this.$emit('goToProfile', this.productId);
    }
  }
}
</script>

<style>
  .product {
    width: 250px;
    height: 270px;

    margin: 15px;
  }

  .product img {
    width: 250px;
    height: 184px;
  }

  .product .name {
    font-family: 'PT Sans', sans-serif;
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 21px;

    color: #000000;

    margin-left: 15px;
  }

  .product .gramms_price {
    display: flex;
    flex-direction: row;
  }

  .product .gramms {
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 11.3208px;
    line-height: 17px;

    color: #7C909C;

    margin: 16px 0 0 15px;
  }

  .product .price_1 {
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

  .product .price {
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 13.6347px;
    line-height: 20px;
    color: #F52341;
  }

  .product--profile {
    display: flex;
    width: 100%;
  }
</style>