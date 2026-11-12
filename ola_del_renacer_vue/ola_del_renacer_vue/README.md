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

## Licencia de PrimeVue 5 (cartel rojo "Invalid PrimeUI License")

PrimeVue 5 exige una clave de licencia; sin ella muestra un cartel rojo abajo a la derecha.
La licencia **Community es gratuita para estudiantes e individuos** (términos: https://primeui.dev/licenses/community).
Cuando tengas tu clave, pégala en `.env` (y en `.env.production`) sin comillas:

```
VUE_APP_PRIMEUI_LICENSE=tu-clave-aqui
```

Reinicia `npm run serve`. El cartel es solo visual: la app funciona igual sin clave.
No subas tu clave a un repositorio público.

## Si el login dice "No se pudo conectar con el servidor"

El navegador no pudo hablar con la API. Revisa:

1. Que la API esté encendida (local: `uvicorn main:app --reload --port 8000`; en Render: estado *Live*).
2. Que `VUE_APP_API_BASE_URL` en `.env` apunte a ella, con `https://` si es Render y sin `/` al final.
   Después de editar `.env` hay que reiniciar `npm run serve`.
3. Que abras la URL de la API en el navegador y responda (en el plan gratuito de Render la primera vez puede tardar cerca de un minuto).
4. La consola del navegador (F12): ahí aparece el motivo real (servidor apagado, URL equivocada o CORS).

## Qué cambió respecto al proyecto original

- Las imágenes del banner, galería, actividades, blog, "conócenos" y login vienen de la API (`/imagenes/{seccion}`).
  Los títulos y textos de Actividades y Blog también.
- El carrusel ahora desliza, tiene flechas y autoplay (en el original el JS del carrusel no existía).
- El login valida contra la API; los tres formularios (contacto, reporte, registrar habitante) guardan en la API.
- Mientras llegan las imágenes se muestran `Skeleton` de PrimeVue (configurado solo con tema claro).
- Cada vista tiene su CSS con `<style scoped>`; lo que estaba en `body` pasó a un contenedor de la vista o a `App.vue`.
- Retoques menores: erratas ("Twitter", "selecciona una red", "aceptar"), el logo conserva su proporción
  (`object-fit: contain`) y los mensajes de los formularios aparecen solo cuando hay texto.
