import os
from datetime import datetime, timezone
from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

app = FastAPI(title="API Ola del Renacer")

# ---------------------------------------------------------------------------
# CORS: permite que el proyecto Vue (otro origen) consuma esta API.
# En Render puedes definir CORS_ORIGINS con la URL de tu frontend, separada
# por comas. Si no la defines, se permiten todos los orígenes (modo práctica).
# ---------------------------------------------------------------------------
origenes = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in origenes],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Las imágenes locales (playa1..playa4) se sirven desde la carpeta static/
# y quedan disponibles en /static/<archivo>
app.mount("/static", StaticFiles(directory="static"), name="static")


# ---------------------------------------------------------------------------
# Datos de las imágenes. Por sección:
#   banner, galeria, actividades, blog, conocenos, login
# Las que empiezan por "static/" son archivos locales de esta API; las demás
# son enlaces externos (los mismos del proyecto original).
# ---------------------------------------------------------------------------
IMAGENES = {
    "banner": [
        {"archivo": "static/playa1.png", "alt": "Playa Santa Marta 1"},
        {"archivo": "static/playa2.png", "alt": "Playa Santa Marta 2"},
        {"archivo": "static/playa3.webp", "alt": "Playa Santa Marta 3"},
        {"archivo": "static/playa4.jpg", "alt": "Playa Santa Marta 4"},
    ],
    "galeria": [
        {
            "archivo": "https://www.santamarta.gov.co/sites/default/files/playa_limpia_1.jpg",
            "alt": "Jornada de limpieza en la playa",
        },
        {
            "archivo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiYmi0wh98Xu9IF5_WW7reUtUOwPR7Qc2IWQ&s",
            "alt": "Actividad del proyecto",
        },
        {
            "archivo": "https://imagenes2.eltiempo.com/files/image_600_455/uploads/2025/04/22/68079839c15a6.jpeg",
            "alt": "Voluntarios del proyecto",
        },
        {
            "archivo": "https://restaurantesrentables.practisis.com/wp-content/uploads/2023/10/hombres-guapos-restaurante-apreton-manos-768x512.jpg",
            "alt": "Alianza con restaurantes",
        },
        {
            "archivo": "https://pasionporsantamarta.com/wp-content/uploads/2021/06/limpieza-playas.jpg",
            "alt": "Primera actividad de limpieza",
        },
        {
            "archivo": "https://www.santamarta.gov.co/sites/default/files/playa_limpia_7.jpg",
            "alt": "Playa limpia",
        },
        {
            "archivo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIaWkGK9xglvBMPyOIsbbY1TNfGDEz11qqBg&s",
            "alt": "Reunión con los primeros trabajadores",
        },
    ],
    "actividades": [
        {
            "archivo": "https://www.paiscircular.cl/wp-content/uploads/2019/03/limpieza-de-playas-5-1024x657.jpg",
            "alt": "Limpieza de playas",
            "titulo": "Limpieza",
            "descripcion": "Salimos y ponemos manos a la obra con nuestro trabajo de limpieza asegurando una buena impresión y mejora en el olor de la zona critica",
        },
        {
            "archivo": "https://www.santamarta.gov.co/sites/default/files/img_4321.jpeg",
            "alt": "Rehabilitación de personas en situación de calle",
            "titulo": "Rehabilitación",
            "descripcion": "Nos ponemos en la tarea de buscar y rehabilitar personas en situacion de calle para que nos ayuden en nuestra labor y darles una segunda oportunidad de comenzar una nueva vida",
        },
        {
            "archivo": "https://wekookacademy.com/wp-content/uploads/2024/08/pexels-sora-shimazaki-5673488.jpg",
            "alt": "Alianza con restaurantes y hoteles",
            "titulo": "Alianza",
            "descripcion": "Nos aliamos con restaurantes y hoteles para mantener limpios los alrededores haciendo que tengan una mejor higiene, presentación y llamen mas la atención",
        },
    ],
    "blog": [
        {
            "archivo": "https://pasionporsantamarta.com/wp-content/uploads/2021/06/limpieza-playas.jpg",
            "alt": "Primera actividad de limpieza",
            "titulo": "Primera actividad de limpieza",
        },
        {
            "archivo": "https://www.santamarta.gov.co/sites/default/files/playa_limpia_7.jpg",
            "alt": "Mejor actividad de limpieza",
            "titulo": "Mejor actividad de limpieza",
        },
        {
            "archivo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIaWkGK9xglvBMPyOIsbbY1TNfGDEz11qqBg&s",
            "alt": "Reunión con primeros trabajadores",
            "titulo": "Reunion con primeros trabajadores",
        },
    ],
    "conocenos": [
        {
            "archivo": "https://travelgrafia.co/wp-content/uploads/2023/10/Playas-en-Santa-Marta-gratis.jpg",
            "alt": "Playa de Santa Marta",
        },
    ],
    "login": [
        {
            "archivo": "https://poporotours.com/wp-content/uploads/2022/04/playacristal-900x600.jpg",
            "alt": "Imagen de una playa",
        },
    ],
}


def url_base(request: Request) -> str:
    """URL pública de la API. En Render conviene definir PUBLIC_URL
    (por ejemplo https://mi-api.onrender.com) para que los enlaces de las
    imágenes locales salgan siempre con https."""
    publica = os.getenv("PUBLIC_URL")
    if publica:
        return publica.rstrip("/")
    return str(request.base_url).rstrip("/")


def armar_url(request: Request, archivo: str) -> str:
    if archivo.startswith("http"):
        return archivo
    return f"{url_base(request)}/{archivo}"


# ---------------------------------------------------------------------------
# Datos en memoria (se pierden si el servicio se reinicia o se duerme)
# ---------------------------------------------------------------------------
contactos = []
reportes = []
beneficiarios = []

USUARIOS = {
    "usuario": {"clave": "123", "rol": "usuario"},
    "admin": {"clave": "admin", "rol": "admin"},
}

ZONAS_REPORTE = {
    1: "Centro Histórico",
    2: "El Rodadero",
    3: "Taganga",
    4: "Bello Horizonte",
    5: "Mamatoco",
    6: "Otro sector",
}

ZONAS_BENEFICIARIO = {
    1: "Centro Histórico",
    2: "El Rodadero",
    3: "Taganga",
}

REDES = {1: "Facebook", 2: "Instagram", 3: "Twitter", 4: "Tiktok"}


def ahora() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Modelos (los nombres de los campos son los que debe enviar el frontend)
# ---------------------------------------------------------------------------
class Login(BaseModel):
    usuario: str = Field(min_length=1)
    contrasena: str = Field(min_length=1)


class Contacto(BaseModel):
    nombre: str = Field(min_length=1)
    correo: str = Field(min_length=1)
    asunto: str = Field(min_length=1)
    comentarios: str = Field(min_length=1)
    tipo_red: int = Field(ge=1, le=4)
    acepto: bool


class Reporte(BaseModel):
    nombre: str = Field(min_length=1)
    correo: str = Field(min_length=1)
    zona: int = Field(ge=1, le=6)
    direccion: str = Field(min_length=1)
    descripcion: str = Field(min_length=1)


class Beneficiario(BaseModel):
    nombre: str = Field(min_length=1)
    zona: int = Field(ge=1, le=3)
    edad: Optional[int] = Field(default=None, ge=0, le=120)
    observaciones: Optional[str] = ""


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------
@app.get("/")
def raiz():
    return {"mensaje": "API Ola del Renacer funcionando", "documentacion": "/docs"}


@app.get("/imagenes/{seccion}")
def listar_imagenes(seccion: str, request: Request):
    if seccion not in IMAGENES:
        raise HTTPException(
            status_code=404,
            detail=f"Sección no encontrada. Opciones: {', '.join(IMAGENES)}",
        )
    resultado = []
    for i, item in enumerate(IMAGENES[seccion], start=1):
        dato = {k: v for k, v in item.items() if k != "archivo"}
        dato["id"] = i
        dato["url"] = armar_url(request, item["archivo"])
        resultado.append(dato)
    return resultado


@app.post("/login")
def iniciar_sesion(datos: Login):
    usuario = USUARIOS.get(datos.usuario)
    if usuario is None or usuario["clave"] != datos.contrasena:
        return {"status": False, "mensaje": "Usuario o contraseña incorrectos"}
    return {"status": True, "rol": usuario["rol"]}


@app.post("/contacto")
def guardar_contacto(datos: Contacto):
    if not datos.acepto:
        raise HTTPException(status_code=400, detail="Debes aceptar los términos")
    registro = datos.model_dump()
    registro["id"] = len(contactos) + 1
    registro["red"] = REDES[datos.tipo_red]
    registro["fecha"] = ahora()
    contactos.append(registro)
    return {"status": True, "id": registro["id"]}


@app.post("/reportes")
def guardar_reporte(datos: Reporte):
    registro = datos.model_dump()
    registro["id"] = len(reportes) + 1
    registro["sector"] = ZONAS_REPORTE[datos.zona]
    registro["fecha"] = ahora()
    reportes.append(registro)
    return {"status": True, "id": registro["id"]}


@app.post("/beneficiarios")
def guardar_beneficiario(datos: Beneficiario):
    registro = datos.model_dump()
    registro["id"] = len(beneficiarios) + 1
    registro["zona_nombre"] = ZONAS_BENEFICIARIO[datos.zona]
    registro["fecha"] = ahora()
    beneficiarios.append(registro)
    return {"status": True, "id": registro["id"]}


@app.get("/resumen")
def resumen():
    """Solo cuenta los registros guardados. No expone datos personales."""
    return {
        "contactos": len(contactos),
        "reportes": len(reportes),
        "beneficiarios": len(beneficiarios),
    }
