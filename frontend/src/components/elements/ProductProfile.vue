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
      </div>
      <div :class="{'counter_price': !isProfileUrl, 'counter_price--profile': isProfileUrl}">
        <div :class="{'counter': !isProfileUrl, 'counter--profile': isProfileUrl}">
          <button class="minus" @click="decrementQuantity">-</button>
          <div class="quantity">{{ product.quantity }}</div>
          <button class="plus" @click="incrementQuantity">+</button>
        </div>
        <div v-if="product.discountedPrice" :class="{'price_1 price_1_2': !isProfileUrl, 'price_1--profile': isProfileUrl}" @click="addToCart">
          <div class="discounted-price" :class="{'price price_2': !isProfileUrl, 'price--profile': isProfileUrl}">{{ product.discountedPrice }} ₽</div>
        </div>
        <div v-else :class="{'price_1': !isProfileUrl, 'price_1--profile': isProfileUrl}" @click="addToCart">
          <div :class="{'price': !isProfileUrl, 'price--profile': isProfileUrl}">{{ product.price }} ₽</div>
        </div>
      </div>
    </div>
    <div v-if="isAdmin" :class="{'admin-buttons': !isProfileUrl, 'admin-buttons--profile_1': isProfileUrl}">
      <button class="admin-buttons--profile" @click="deleteProduct">Удалить</button>
      <button class="admin-buttons--profile" @click="editProduct">Редактировать</button>
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
      isProfileUrl: false,
      isAdmin: false
    }
  },
  mounted() {
    this.getProduct();
    this.checkUrl();
    this.checkAdminStatus();
  },
  methods: {
    async getProduct() {
      try {
        const response = await axios.get(`http://localhost:8000/api/products/${this.productId}/`);
        const data = response.data;
        this.product = data;
        this.product.quantity = 1;
        await this.getDiscount();

        if (localStorage.getItem('access_token')) {
          const token = localStorage.getItem('access_token');
          const authResponse = await axios.get('http://localhost:8000/api/core/auth/', {
            headers: {
              Authorization: `Bearer ${token}`
            }
          });

          if (authResponse.data.is_staff) {
            this.isAdmin = true;
          }
        }
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
    },
    async getDiscount() {
      try {
        const response = await fetch(`http://localhost:8000/api/discounts/?product=${this.productId}`);
        if (!response.ok) {
          throw new Error(response.status + ' ' + response.statusText);
        }
        const data = await response.json();
        if (data.length > 0) {
          const discount = data[0];
          const discountPrice = this.product.price - (this.product.price * (discount.discount_percentage / 100));
          this.product.discountedPrice = discountPrice.toFixed(2);
        }
      } catch (error) {
        console.error(error);
      }
    },
    checkAdminStatus() {
      const token = localStorage.getItem('access_token');
      axios.get('http://localhost:8000/api/core/auth/', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      .then(response => {
        const isStaff = response.data.role;
        this.isAdmin = isStaff;
      })
      .catch(error => {
        console.error('Failed to get admin status', error);
      });
    },

    deleteProduct() {
      if (confirm('Вы уверены, что хотите удалить товар?')) {
        const token = localStorage.getItem('access_token');
        const url = `http://localhost:8000/api/products/${this.product.id}/delete/`;

        axios
            .delete(url, {
              headers: {
                Authorization: `Bearer ${token}`,
              },
            })
            .then(response => {
              if (response.data.success) {
                alert('Product deleted successfully!');
                this.$router.push('/');
              } else {
                alert('Failed to delete product: ' + response.data.message);
              }
            })
            .catch(error => {
              console.error('Failed to delete product', error);
            });
      }
    },

    editProduct() {
      this.$router.push(`${this.product.id}/edit/`)
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

    margin: -25px 15px 0 auto;

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

  .price_1_2 {
    background: #ffa600;
  }

  .price_2 {
    color: #FAFAFA;
  }

  .description, .header, .list, .counter, .admin-buttons {
    display: none;
  }

  .product--profile {
    display: flex;
    flex-direction: row;

    width: 400px;
    height: 340px;

    margin: 40px 15px 0 15px;
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

    margin-bottom: 15px;
  }

  .gramms--profile {
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 21px;

    color: #7C909C;

    margin-bottom: 15px;
  }

  .description--profile {
    font-family: 'Poppins', sans-serif;
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 21px;

    color: #2F2F2F;

    margin-bottom: 160px;
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

    margin: 8px 0 0 70px;
  }

  .counter--profile {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .quantity {
    padding: 20px 10px 0 10px;
  }

  .quantity, minus, plus {
    height: 38px;

    font-size: 16px;
    font-weight: bold;
  }

  .minus, .plus {
    border: 3px solid #F52341;
    background: #FFFFFF;
  }

  .content--profile {
    display: flex;
    flex-direction: column;
    text-align: left;

    margin: 0 0 0 40px;
  }

  .counter_price--profile {
    display: flex;
    flex-direction: row;
  }

  .admin-buttons--profile {
    padding: 8px 16px;
    background-color: #dc3545;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;

    margin: 10px;
  }

  .admin-buttons--profile:hover {
    background-color: #c82333;
  }
</style>