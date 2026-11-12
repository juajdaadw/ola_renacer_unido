# API Ola del Renacer

API en FastAPI que alimenta el proyecto Vue `ola_del_renacer_vue`.
Está separada del proyecto Vue a propósito: se despliega por su cuenta (por ejemplo en Render).

## Ejecutar en tu computador

```
python -m venv .venv
.venv\Scripts\activate          # en Windows
source .venv/bin/activate       # en Mac / Linux
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

- API: http://localhost:8000
- Documentación interactiva (probar endpoints): http://localhost:8000/docs

## Endpoints

| Método | Ruta | Para qué sirve |
|---|---|---|
| GET | `/` | Comprobar que la API responde |
| GET | `/imagenes/{seccion}` | Lista de imágenes. Secciones: `banner`, `galeria`, `actividades`, `blog`, `conocenos`, `login` |
| POST | `/login` | Recibe `usuario` y `contrasena`; responde `status` y `rol` (sin token) |
| POST | `/contacto` | Guarda el formulario de contacto del Home |
| POST | `/reportes` | Guarda un reporte de zona sucia |
| POST | `/beneficiarios` | Guarda un habitante de calle (vista de admin) |
| GET | `/resumen` | Cuenta cuántos registros hay guardados (sin mostrar datos personales) |

Usuarios de prueba (los mismos del proyecto original): `usuario` / `123` y `admin` / `admin`.

`actividades` y `blog` devuelven además `titulo` (y `descripcion` en actividades).
Las imágenes `playa1` a `playa4` están en la carpeta `static/` y se sirven en `/static/...`.

## Desplegar en Render

1. Sube esta carpeta a un repositorio de GitHub (solo esta carpeta, no el proyecto Vue).
2. En Render crea un **Web Service** conectado a ese repositorio.
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT --proxy-headers --forwarded-allow-ips="*"`
5. Variables de entorno recomendadas:
   - `PUBLIC_URL` = la URL de tu servicio, por ejemplo `https://tu-api.onrender.com` (para que las imágenes locales salgan con `https`).
   - `CORS_ORIGINS` = la URL de tu frontend (opcional; si no la defines se permiten todos los orígenes).

## Importante

- Los datos de contacto, reportes y beneficiarios se guardan **en memoria**: se pierden cuando Render reinicia o duerme el servicio.
- No hay token: el rol `admin` solo controla qué botones muestra el frontend. Cualquiera que conozca la URL de la API puede llamar a los endpoints.
- Por privacidad no existen endpoints para listar los beneficiarios, reportes ni contactos.
- `playa1.png` (3.2 MB) y `playa2.png` (2.3 MB) son pesadas. Si el banner tarda en cargar, conviértelas a `.webp`.
