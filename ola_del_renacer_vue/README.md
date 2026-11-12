# Ola del Renacer (Vue)

Migración a Vue 3 (Vue CLI, Options API) del proyecto HTML/CSS/JS "ola del renacer".
Sigue la misma estructura del proyecto `antes_parcial` del profesor: `vue-router`, `axios` + `vue-axios`,
URL de la API en una variable de entorno y PrimeVue (solo `Skeleton`).

La API está en una carpeta aparte: `ola_del_renacer_api`. **Enciéndela antes de abrir este proyecto.**

## Ejecutar

```
npm install
npm run serve
```

La URL de la API se lee de `VUE_APP_API_BASE_URL`:

| Archivo | Cuándo se usa | Valor |
|---|---|---|
| `.env` | `npm run serve` (desarrollo) | `http://localhost:8000` |
| `.env.production` | `npm run build` | `https://api-vue-jzj4.onrender.com` (la API en Render) |

Después de editar un `.env` hay que reiniciar `npm run serve`.

## Vistas y rutas

| Ruta | Vista | Antes |
|---|---|---|
| `/login` (y `/`) | `LoginView.vue` | `login.html` |
| `/home` | `HomeView.vue` | `Inicio.html` |
| `/galeria` | `GaleriaView.vue` | `galeria.html` |
| `/reportar-zona` | `ReportarZonaView.vue` | `Zona.html` |
| `/registrar-habitante` | `RegistrarHabitanteView.vue` | `Beneficiario.html` |

Componente adicional: `CarruselComponent.vue` (adaptado del carrusel del profesor, con tus puntitos).

## Usuarios de prueba

- `usuario` / `123`
- `admin` / `admin`

## Sesión con token

Mismo patrón visto en clase:

1. `LoginView`: si `response.data.status` es `true`, guarda `token` y `rol` en `localStorage` y va a `/home`.
   La contraseña nunca se guarda.
2. Cada llamada protegida envía el token como último argumento de axios:
   `{ headers: { Authorization: 'Bearer ' + localStorage.getItem('token') } }`.
   Hoy la única es `POST /beneficiarios` en `RegistrarHabitanteView` (exige rol `admin` en la API).
3. "CERRAR SESIÓN" (en el Home, visible solo con sesión iniciada): llama a `POST /logout`, borra `token` y `rol`
   de `localStorage` aunque la llamada falle, y va a `/login`.
4. En `RegistrarHabitanteView`: si la API responde **401** (sin token, vencido o la API se reinició) se borra la sesión
   y se va a `/login`; si responde **403** se muestra "No tienes permiso para registrar habitantes".

`/registrar-habitante` tiene `meta: { requiereToken: true }` y un `router.beforeEach` manda a `/login` si no hay token.
Eso, igual que `v-show="esAdmin"` en el botón "REGISTRAR HABITANTE DE CALLE", es **solo visual**: quien decide de verdad
es la API, que saca el rol del token guardado en el servidor.

El token dura 2 horas y vive en la memoria de la API: si Render duerme o reinicia el servicio, hay que iniciar sesión otra vez.
