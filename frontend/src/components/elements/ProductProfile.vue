<template>
  <div :class="{'header': !isProfileUrl, 'header--profile': isProfileUrl}">
    <hea-der />
  </div>
  <div :class="{'list': !isProfileUrl, 'list--profile': isProfileUrl}">
    <category-list />
  </div>
  <div :class="{'product': !isProfileUrl, 'product--profile': isProfileUrl}" @click="navigateToProfile">
    <img :src="product.image" alt="product image" :class="{'img': !isProfileUrl, 'img--profile': isProfileUrl}">
    <div :class="{'name': !isProfileUrl, 'name--profile': isProfileUrl}">{{ product.name }}</div>
    <div :class="{'gramms_price': !isProfileUrl, 'gramms_price--profile': isProfileUrl}">
      <div :class="{'gramms': !isProfileUrl, 'gramms--profile': isProfileUrl}">{{ product.gramms }} гр.</div>
      <div :class="{'price_1': !isProfileUrl, 'price_1--profile': isProfileUrl}">
        <div :class="{'price': !isProfileUrl, 'price--profile': isProfileUrl}">{{ product.price }} ₽</div>
      </div>
    </div>
    <div :class="{'description': !isProfileUrl, 'description--profile': isProfileUrl}">{{product.description}}</div>
  </div>
</template>

<script>
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";
export default {
  name: 'ProductProfile',
  components: {CategoryList, HeaDer},
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

  .img {
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

  .description, .header, .list {
    display: none;
  }

  .product--profile {
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  .gramms_price--profile {
    display: flex;
    flex-direction: column;
  }
</style>