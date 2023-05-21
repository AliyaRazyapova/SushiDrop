<template>
  <div :class="{'header': !isProfileUrl, 'header--profile': isProfileUrl}">
    <hea-der />
  </div>
  <div :class="{'list': !isProfileUrl, 'list--profile': isProfileUrl}">
    <category-list />
  </div>
  <div :class="{'product': !isProfileUrl, 'product--profile': isProfileUrl}" @click="navigateToProfile">
    <img :src="product.image" alt="product image" :class="{'img': !isProfileUrl, 'img--profile': isProfileUrl}">
    <div :class="{'content': !isProfileUrl, 'content--profile': isProfileUrl}">
      <div :class="{'name': !isProfileUrl, 'name--profile': isProfileUrl}">{{ product.name }}</div>
      <div :class="{'gramms_price': !isProfileUrl, 'gramms_price--profile': isProfileUrl}">
        <div :class="{'gramms': !isProfileUrl, 'gramms--profile': isProfileUrl}">{{ product.gramms }} гр.</div>
        <div :class="{'description': !isProfileUrl, 'description--profile': isProfileUrl}">{{product.description}}</div>
        <div :class="{'price_1': !isProfileUrl, 'price_1--profile': isProfileUrl}" @click="addToCart">
          <div :class="{'price': !isProfileUrl, 'price--profile': isProfileUrl}">{{ product.price }} ₽</div>
        </div>
        <div :class="{'counter': !isProfileUrl, 'counter--profile': isProfileUrl}">
          <button class="minus" @click="decrementQuantity">-</button>
          <div class="quantity">{{ product.quantity }}</div>
          <button class="plus" @click="incrementQuantity">+</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";
import axios from "axios";

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
        this.product.quantity = 1;
      } catch (error) {
        console.error(error);
      }
    },
    checkUrl() {
      this.isProfileUrl = this.$route.name === 'ProductProfile' && this.$route.params.productId == this.productId;
    },
    navigateToProfile() {
      this.$emit('goToProfile', this.productId);
    },
    incrementQuantity() {
      this.product.quantity++;
    },
    decrementQuantity() {
      if (this.product.quantity > 0) {
        this.product.quantity--;
      }
    },
    addToCart() {
      if (this.product.quantity > 0) {
        const cartItem = {
          product: this.product.id,
          quantity: this.product.quantity
        };
        const token = localStorage.getItem('access_token')

        axios.post('http://localhost:8000/api/cart/add/', cartItem, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
          .then(response => {
            if (response.data.success) {
              alert('Product added to cart successfully!');
              this.product.quantity = 0;
            } else {
              alert('Failed to add product to cart: ' + response.data.message);
            }
          })
          .catch(error => {
            console.error('Failed to add product to cart', error);
          });
      }
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

  .description, .header, .list, .counter {
    display: none;
  }

  .product--profile {
    display: flex;
    flex-direction: row;

    width: 400px;
    height: 340px;

    margin: 15px;
  }

  .img--profile {
    width: 100%;
    height: 100%;
  }

  .name--profile {
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 24px;
    line-height: 36px;

    color: #000000;
  }

  .gramms--profile {
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 21px;

    color: #7C909C;
  }

  .description--profile {
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 21px;

    color: #2F2F2F;
  }

  .price--profile {
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 15.0103px;
    line-height: 23px;

    margin: auto;

    color: #FFFFFF;
  }

  .price_1--profile {
    display: flex;

    width: 182px;
    height: 38px;

    background: #E30538;
    border-radius: 9.38144px;
  }
</style>