import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import HomeView from '../views/HomeView.vue'
import GaleriaView from '../views/GaleriaView.vue'
import ReportarZonaView from '../views/ReportarZonaView.vue'
import RegistrarHabitanteView from '../views/RegistrarHabitanteView.vue'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/galeria',
    name: 'galeria',
    component: GaleriaView
  },
  {
    path: '/reportar-zona',
    name: 'reportar-zona',
    component: ReportarZonaView
  },
  {
    path: '/registrar-habitante',
    name: 'registrar-habitante',
    component: RegistrarHabitanteView,
    meta: { requiereToken: true }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Solo comodidad visual: la seguridad real la hace la API
router.beforeEach((to) => {
  if (to.meta.requiereToken && !localStorage.getItem('token')) {
    return '/login';
  }
})

export default router
