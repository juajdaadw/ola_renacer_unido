import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Importar axios
import axios from 'axios'
import VueAxios from 'vue-axios'

// URL base de la API (viene de .env en desarrollo y de .env.production al compilar)
axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL;

//Importar Prime Vue
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';

import Skeleton from 'primevue/skeleton';

import CarruselComponent from './components/CarruselComponent.vue'

const app = createApp(App).use(router);
//Uso de axios
app.use(VueAxios, axios);

//Usar Prime-Vue
app.use(PrimeVue, {
    theme: {
        preset: Aura,
        options: {
            darkModeSelector: false
        }
    },
});

app.component("SkeletonPrime", Skeleton);
app.component("CarruselComponent", CarruselComponent);

app.mount('#app');
