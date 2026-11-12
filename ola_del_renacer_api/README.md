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
| POST | `/login` | Recibe `usuario` y `contrasena`; responde `status`, `rol` y `token` |
| POST | `/logout` | **Requiere token.** Invalida el token enviado |
| POST | `/contacto` | Guarda el formulario de contacto del Home |
| POST | `/reportes` | Guarda un reporte de zona sucia |
| POST | `/beneficiarios` | **Requiere token de `admin`.** Guarda un habitante de calle |
| GET | `/resumen` | Cuenta cuántos registros hay guardados (sin mostrar datos personales) |

Usuarios de prueba (los mismos del proyecto original): `usuario` / `123` y `admin` / `admin`.

## Autenticación con token

1. `POST /login` con usuario y contraseña correctos responde `{"status": true, "rol": "...", "token": "..."}`.
   Si fallan, responde `{"status": false, "mensaje": "..."}` como antes.
2. El token es una cadena aleatoria (`secrets.token_urlsafe(32)`) que dura **2 horas**.
   La API lo guarda en el diccionario `SESIONES` (token → usuario, rol y expiración) y borra los vencidos.
3. Las llamadas protegidas envían la cabecera `Authorization: Bearer <token>`.
4. `POST /logout` (con la misma cabecera) borra el token del servidor.

Endpoints protegidos (dependencias `verificar_token` y `verificar_admin` en `main.py`):

| Endpoint | Exige | Sin token / token inválido o vencido | Token válido sin rol `admin` |
|---|---|---|---|
| `POST /beneficiarios` | token de `admin` | 401 | 403 |
| `POST /logout` | cualquier token válido | 401 | — |

`/`, `/login`, `/imagenes/{seccion}`, `/contacto`, `/reportes` y `/resumen` siguen siendo públicos.
El rol se toma siempre del token guardado en el servidor, nunca de lo que envíe el cliente.

Para probar en `/docs`: haz login, copia el `token` y en el campo `authorization` del endpoint escribe `Bearer <token>`.

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
- Los tokens también viven **en memoria**: cuando la API se reinicia (por ejemplo cuando Render duerme el servicio) todos se pierden
  y hay que volver a iniciar sesión. El frontend lo detecta (responde 401) y manda al login.
- La API nunca imprime ni registra los tokens.
- Por privacidad no existen endpoints para listar los beneficiarios, reportes ni contactos.
- `playa1.png` (3.2 MB) y `playa2.png` (2.3 MB) son pesadas. Si el banner tarda en cargar, conviértelas a `.webp`.
