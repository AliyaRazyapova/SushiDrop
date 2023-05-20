import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'process/browser';

const app = createApp(App)
app.use(router)
app.mount('#app')
