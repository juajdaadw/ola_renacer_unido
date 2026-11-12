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
| `.env.production` | `npm run build` | **Cámbiala** por la URL real de tu API en Render |

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

El botón "REGISTRAR HABITANTE DE CALLE" del Home usa `v-show="esAdmin"`: solo se muestra con el rol `admin`.
Sin tokens (como se pidió), el rol se guarda en `localStorage` y `v-show` solo oculta el botón; no protege la ruta.
