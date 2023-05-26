<template>
  <hea-der />
  <category-list />
  <div class="cart-container">
    <h1 class="cart-heading">Корзина</h1>
    <div v-if="cartItems.length === 0">
      <p class="empty-cart-message">Ваша корзина пуста.</p>
    </div>
    <div v-else>
      <table class="cart-table">
        <thead>
          <tr>
            <th>Изображение</th>
            <th>Продукт</th>
            <th>Цена</th>
            <th>Количество</th>
            <th>Общая стоимость</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in groupedCartItems" :key="item.id">
            <td>
              <img :src="item.product.image" alt="Product Image" class="product-image" />
            </td>
            <td>{{ item.product.name }}</td>
            <td>{{ item.product.price }}{{ item.product.discount ? ` (скидка ${item.product.discount}%)` : '' }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ item.totalPrice }}</td>
          </tr>
        </tbody>
      </table>
      <div class="total-cost">Общая стоимость: {{ totalCost }}</div>
      <div class="button-container">
        <button @click="clearCart" class="clear-button">Очистить корзину</button>
      </div>
      <div class="order-button-container">
        <button @click="proceedToOrderPage" class="order-button">Оформить заказ</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import HeaDer from "@/components/elements/HeaDer";
import CategoryList from "@/components/elements/CategoryList";

export default {
  components: {CategoryList, HeaDer},
  data() {
    return {
      cartItems: [],
    };
  },
  mounted() {
    this.getCartItems();
  },
  methods: {
    getCartItems() {
      const token = localStorage.getItem('access_token');
      const headers = {
        Authorization: `Bearer ${token}`,
      };

      axios
        .get('http://localhost:8000/api/cart/', { headers })
        .then((response) => {
          console.log(response.data);
          const cartItems = response.data;

          const groupedItems = {};

          cartItems.forEach((item) => {
            if (item.product in groupedItems) {
              groupedItems[item.product].quantity += item.quantity;
            } else {
              groupedItems[item.product] = {
                id: item.id,
                user: item.user,
                product: null,
                quantity: item.quantity,
              };
            }
          });

          const promises = [];

          Object.keys(groupedItems).forEach((productId) => {
            const promise = axios.get(`http://localhost:8000/api/products/${productId}/`, { headers });
            promises.push(promise);
          });

          Promise.all(promises)
            .then((responses) => {
              responses.forEach((response, index) => {
                const productId = Object.keys(groupedItems)[index];
                groupedItems[productId].product = response.data;
              });

              const cartItemsWithProduct = Object.values(groupedItems);

              const discountPromises = cartItemsWithProduct.map((item) =>
                axios.get(`http://localhost:8000/api/discounts/?product=${item.product.id}`, { headers })
              );

              Promise.all(discountPromises)
                .then((discountResponses) => {
                  discountResponses.forEach((response, index) => {
                    const discounts = response.data;
                    if (discounts.length > 0) {
                      const productId = Object.keys(groupedItems)[index];
                      const item = groupedItems[productId];

                      const discount = discounts[0];
                      const discountedPrice = item.product.price * (1 - discount.discount_percentage / 100);
                      item.product.price = discountedPrice.toFixed(2);
                    }
                  });

                  cartItemsWithProduct.forEach((item) => {
                    item.totalPrice = item.product.price * item.quantity;
                  });

                  this.cartItems = cartItemsWithProduct;
                })
                .catch((error) => {
                  console.error('Failed to fetch discounts', error);
                });
            })
            .catch((error) => {
              console.error('Failed to fetch product', error);
            });
        })
        .catch((error) => {
          console.error('Failed to fetch cart items', error);
        });
    },
    proceedToOrderPage() {
      const orderData = {
        orderItems: JSON.stringify(this.groupedCartItems),
        total_price: this.totalCost,
      };
      console.log(orderData);
      this.$router.push({ name: 'OrdersPage', query: orderData });
    },
    clearCart() {
      const token = localStorage.getItem('access_token');
      const headers = {
        Authorization: `Bearer ${token}`,
      };

      axios
        .delete('http://localhost:8000/api/cart/delete/', { headers })
        .then(() => {
          this.cartItems = [];
          console.log('Cart cleared successfully.');
        })
        .catch((error) => {
          console.error('Failed to clear cart', error.response.data);
        });
    },
  },
  computed: {
    groupedCartItems() {
      const groupedItems = {};

      this.cartItems.forEach((item) => {
        const productId = item.product.id;
        if (productId in groupedItems) {
          groupedItems[productId].quantity += item.quantity;
          groupedItems[productId].totalPrice += item.totalPrice;
        } else {
          groupedItems[productId] = {
            id: item.id,
            user: item.user,
            product: item.product,
            quantity: item.quantity,
            totalPrice: item.totalPrice,
          };
        }
      });

      return Object.values(groupedItems);
    },
    totalCost() {
      return this.groupedCartItems.reduce((total, item) => total + item.totalPrice, 0);
    },
  },
};
</script>

<style scoped>
  .cart-container {
    background-color: #ffffff;
    color: #000000;
    padding: 20px;
  }

  .cart-heading {
    text-align: center;
    font-size: 28px;
    margin-bottom: 40px;
  }

  .empty-cart-message {
    text-align: center;
    font-size: 18px;
    margin-bottom: 20px;
  }

  .cart-table {
    width: 100%;
    border-collapse: collapse;
  }

  .cart-table th,
  .cart-table td {
    padding: 8px;
    text-align: center;
    border-bottom: 1px solid #000000;
  }

  .cart-table th {
    background-color: #f0f0f0;
  }

  .product-image {
    width: 100px;
    height: 100px;
    object-fit: cover;
  }

  .total-cost {
    font-weight: bold;
    margin-top: 20px;
    text-align: right;
  }

  .order-button-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
  }

  .order-button {
    font-weight: bold;
    font-size: 16px;
    padding: 12px 24px;
    background-color: #F52341;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .order-button:hover {
    background-color: #333333;
  }

  .button-container {
    display: flex;
    justify-content: flex-start;
    margin-top: 20px;
  }

  .clear-button {
    font-weight: bold;
    font-size: 16px;
    padding: 12px 24px;
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #000000;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .clear-button:hover {
    background-color: #000000;
    color: #ffffff;
  }
</style>
