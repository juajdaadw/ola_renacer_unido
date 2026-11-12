<template>
    <div class="pagina-home">
        <!--HEADER-->
        <header class="header">
            <h1><img class="logo" src="../assets/LOGO-sinfondo.png" alt="Logo"></h1>
            <menu class="menu">
                <div class="opciones">INICIO</div>
                <div class="opciones">CONOCENOS</div>
                <div class="opciones">ACTIVIDADES</div>
                <div class="opciones">GALERIA</div>
                <div class="opciones">BLOG</div>
                <div class="opciones">CONTACTO</div>
            </menu>
        </header>
        <!-- ============================================================================================================ -->

        <p v-if="errorApi" class="error-api">{{ errorApi }}</p>

        <!--BANNER-->
        <CarruselComponent :slides="urlsBanner" :cargando="cargando" />

        <!-- ============================================================================================================ -->

        <!--CONOCENOS-->
        <section class="inicio">
            <h2>CONOCENOS</h2>
            <div class="separador">
                <div class="algo">
                    <div class="sobre-nosotros">Nuestro modelo de negocio social se basa en la intervención de puntos
                        críticos y turísticos de la ciudad de Santa Marta donde las empresas tradicionales de aseo no
                        llegan
                    </div>
                    <div class="mision">
                        <div>
                            <h3>MISION</h3>
                            <p class="parrafo">Contribuir a la limpieza y recuperación de zonas turísticas y críticas de
                                Santa Marta mediante un modelo social que capacita y emplea a habitantes de calle en
                                labores de aseo, reciclaje y atención al turista, promoviendo inclusión social y cuidado
                                ambiental.
                            </p>
                        </div>
                        <div>
                            <h3>VISION</h3>
                            <p class="parrafo">Convertirse en un modelo social sostenible de impacto ambiental y social
                                en Santa Marta, donde los habitantes de calle se transformen en guardianes de la ciudad
                                y el proyecto sea un referente de inclusión y cuidado de los espacios turísticos.</p>
                        </div>
                        <div>
                            <h3>VALORES</h3>
                            <ul class="parrafo">
                                <li>Inclusión social: dar oportunidades a habitantes de calle</li>
                                <li>Responsabilidad ambiental: mantener limpias zonas críticas y turísticas.</li>
                                <li>Dignidad humana: eliminar el estigma social hacia esta población.</li>
                                <li>Compromiso comunitario: trabajar con comercios, turistas y la alcaldía.</li>
                                <li>Solidaridad: promover apoyo de donantes y aliados para el proyecto.</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="img1">
                    <SkeletonPrime v-if="cargando" width="100%" height="100%" />
                    <img v-else-if="conocenos" :src="conocenos.url" :alt="conocenos.alt" width="100%" height="100%"
                        style="border: solid gray 3px;">
                </div>
            </div>
        </section>

        <!-- ============================================================================================================ -->

        <!--ACTIVIDADES-->
        <section class="actividades">
            <h2>NUESTRAS ACTIVIDADES</h2>
            <div class="acts">
                <template v-if="cargando">
                    <div v-for="n in 3" :key="n" class="cuadros">
                        <SkeletonPrime width="100%" height="250px" />
                        <SkeletonPrime width="40%" height="1.5rem" />
                        <SkeletonPrime width="100%" height="3rem" />
                    </div>
                </template>
                <template v-else>
                    <div v-for="actividad in actividades" :key="actividad.id" class="cuadros">
                        <img :src="actividad.url" :alt="actividad.alt" width="100%" height="250px">
                        <h2>{{ actividad.titulo }}</h2>
                        <p>{{ actividad.descripcion }}</p>
                    </div>
                </template>
            </div>
        </section>

        <!-- ============================================================================================================ -->

        <!--GALERIA y el BLOG-->
        <section class="inicio">
            <div class="contenedor-galeria">
                <div class="galeria">
                    <h2 class="linea h2">Galeria de fotos</h2>
                    <template v-if="cargando">
                        <div v-for="n in 4" :key="n">
                            <SkeletonPrime width="90%" height="300px" />
                        </div>
                    </template>
                    <template v-else>
                        <div v-for="foto in galeriaDestacada" :key="foto.id">
                            <img :src="foto.url" :alt="foto.alt" width="90%" height="300px">
                        </div>
                    </template>
                    <button class="boton-otro" @click="irAGaleria">VER MAS</button>
                </div>
                <div class="blog">
                    <h2 class="linea" style="padding-top: 3px;">Blog</h2>
                    <template v-if="cargando">
                        <div v-for="n in 3" :key="n" class="cont1">
                            <SkeletonPrime width="170px" height="170px" />
                            <SkeletonPrime width="60%" height="2rem" />
                        </div>
                    </template>
                    <template v-else>
                        <div v-for="entrada in blog" :key="entrada.id" class="cont1">
                            <img :src="entrada.url" :alt="entrada.alt" width="170px" height="170px"
                                style="padding-top: 20px;">
                            <div style="padding-top: 50px;">{{ entrada.titulo }}</div>
                        </div>
                    </template>
                </div>
            </div>
        </section>

        <!-- ============================================================================================================ -->

        <footer class="inicio-nc" style="margin-top: 90px;">

            <div class="contactanos">
                <h2>CONTACTANOS</h2>
                <input v-model="contacto.nombre" placeholder=" Digite nombre..." class="cuadritos-inp">
                <input v-model="contacto.correo" placeholder=" Ingresa tu correo electronico " class="cuadritos-inp">
                <input v-model="contacto.asunto" placeholder=" Asunto por el cual nos contactas" class="cuadritos-inp">
                <input v-model="contacto.comentarios" placeholder=" Describe el asunto" class="cuadritos-inp">
                <select v-model="contacto.tipoRed" class="cuadritos-inp">
                    <option :value="0">Seleccione tipo de red social la cual nos ubicaste</option>
                    <option :value="1">Facebook</option>
                    <option :value="2">Instagram</option>
                    <option :value="3">Twitter</option>
                    <option :value="4">Tiktok</option>
                </select>
                <div style="display: flex;">
                    <input id="chk-acepto" v-model="contacto.acepto" class="checkbox" type="checkbox">
                    <label class="chk-acepto" for="chk-acepto">Acepto los terminos</label>
                </div>
                <button :disabled="enviando" class="btn-enviar" @click="enviarContacto">
                    {{ enviando ? 'enviando...' : 'enviar' }}
                </button>
            </div>

            <div v-if="exito" class="success">{{ exito }}</div>
            <div v-if="advertencia" class="warning">{{ advertencia }}</div>

            <button class="boton-otro" style="margin-top: 20px; margin-left: 0;" @click="irAReporte">REPORTAR ZONA
                CRÍTICA</button>

            <!-- Solo lo ve el administrador -->
            <button v-show="esAdmin" class="boton-otro" style="margin-top: 20px; margin-left: 0;"
                @click="irARegistro">REGISTRAR HABITANTE DE CALLE</button>

        </footer>
    </div>
</template>

<script>
export default {
    name: 'HomeView',
    data() {
        return {
            rol: '',

            cargando: false,
            errorApi: '',
            banner: [],
            galeria: [],
            actividades: [],
            blog: [],
            conocenos: null,

            contacto: {
                nombre: '',
                correo: '',
                asunto: '',
                comentarios: '',
                tipoRed: 0,
                acepto: false
            },
            enviando: false,
            advertencia: '',
            exito: ''
        };
    },
    computed: {
        esAdmin() {
            return this.rol === 'admin';
        },
        urlsBanner() {
            return this.banner.map(imagen => imagen.url);
        },
        galeriaDestacada() {
            return this.galeria.slice(0, 4);
        }
    },
    methods: {
        async cargarContenido() {
            this.cargando = true;
            this.errorApi = '';
            try {
                const [banner, galeria, actividades, blog, conocenos] = await Promise.all([
                    this.axios.get('/imagenes/banner'),
                    this.axios.get('/imagenes/galeria'),
                    this.axios.get('/imagenes/actividades'),
                    this.axios.get('/imagenes/blog'),
                    this.axios.get('/imagenes/conocenos')
                ]);
                this.banner = banner.data;
                this.galeria = galeria.data;
                this.actividades = actividades.data;
                this.blog = blog.data;
                this.conocenos = conocenos.data[0];
            } catch (e) {
                console.log(e);
                this.errorApi = 'No se pudieron cargar las imágenes. Revisa que la API esté encendida e intenta de nuevo.';
            } finally {
                this.cargando = false;
            }
        },

        async enviarContacto() {
            const c = this.contacto;
            this.exito = '';

            if (c.nombre === '') {
                this.advertencia = 'Por favor digite un nombre';
                return;
            }
            if (c.correo === '') {
                this.advertencia = 'Por favor digite un correo';
                return;
            }
            if (c.asunto === '') {
                this.advertencia = 'Por favor digite un asunto';
                return;
            }
            if (c.comentarios === '') {
                this.advertencia = 'Por favor escriba un comentario';
                return;
            }
            if (c.tipoRed === 0) {
                this.advertencia = 'Por favor selecciona una red';
                return;
            }
            if (!c.acepto) {
                this.advertencia = 'Debes aceptar los terminos y condiciones';
                return;
            }

            this.advertencia = '';
            this.enviando = true;
            try {
                await this.axios.post('/contacto', {
                    nombre: c.nombre,
                    correo: c.correo,
                    asunto: c.asunto,
                    comentarios: c.comentarios,
                    tipo_red: c.tipoRed,
                    acepto: c.acepto
                });
                this.exito = 'Has completado la informacion con exito';
                this.contacto = { nombre: '', correo: '', asunto: '', comentarios: '', tipoRed: 0, acepto: false };
            } catch (e) {
                console.log(e);
                this.advertencia = 'No se pudo enviar el formulario. Intenta de nuevo';
            } finally {
                this.enviando = false;
            }
        },

        irAGaleria() {
            this.$router.push('/galeria');
        },
        irAReporte() {
            this.$router.push('/reportar-zona');
        },
        irARegistro() {
            this.$router.push('/registrar-habitante');
        }
    },
    created() {
        this.rol = localStorage.getItem('rol');
    },
    mounted() {
        this.cargarContenido();
    }
};
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}

.logo {
    width: 100%;
    height: 80px;
    object-fit: contain;
}


.header {
    height: 80px;
    display: grid;
    grid-template-columns: 1fr 5fr 1fr;
    justify-content: center;
    align-items: center;
    gap: 1rem 6rem;
    padding-left: 50px;
    background-color: #3ca9d0;
    border-bottom: solid black 3px;
}

.menu {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
    font-weight: 900;
}

.opciones:hover {
    color: white;
    cursor: pointer;
}

.error-api {
    background-color: lightcoral;
    color: red;
    padding: 10px 50px;
    text-align: center;
}

.botones {
    width: 250px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    justify-content: center;
    align-items: center;
}

.boton {
    background-color: dimgray;
    color: white;
    border-radius: 10px;
    height: 30px;
    width: 120px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.boton:hover {
    cursor: pointer;
    background-color: white;
    color: dimgray;
}

.inicio {
    height: 700px;
    width: 97%;
    padding-left: 50px;
    padding-top: 50px;
}

.separador {
    display: grid;
    grid-template-columns: 3fr 1fr;
    height: 590px;
    width: 99%;
    padding-top: 50px;
}

.sobre-nosotros {
    height: 170px;
    width: 90%;
    font-size: 30px;
    display: grid;
    justify-content: center;
    align-items: end;
    padding-left: 20px;
    padding-bottom: 30px;
    border-bottom: solid black 3px;
}

.mision {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    grid-row-start: 2;
    grid-row-end: 3;
    padding-bottom: 80px;
    padding-left: 50px;
    width: 90%;
    height: 53%;
    padding-top: 20px;
}

.parrafo {
    font-size: 19px;
    width: 240px;
    height: 100px;
}

.img1 {
    width: 600px;
    height: 700px;
    grid-column-start: 2;
    grid-column-end: 3;
    margin-top: -100px;
}

.algo {
    display: flexbox;
}

.actividades {
    height: 500px;
    width: 97%;
    padding-left: 50px;
    padding-top: 50px;
}


.acts {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    column-gap: 10px;
}

.linea {
    border-bottom: solid gray 3px;
    padding-bottom: 10px;
}

.cuadros {
    display: grid;
    grid-template-rows: 3fr 1fr 1fr 1fr;
    width: 25%;
    height: 400px;
    justify-content: center;
    align-items: center;
    margin-top: 30px;
}

.contenedor-galeria {
    display: flex;
    height: 600px;

}

.galeria {
    width: 50%;
    display: grid;
    padding-left: 10px;
    align-items: center;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr 1fr;
    row-gap: 20px;
    padding-top: 2px;
}

.blog {
    width: 50%;
    padding-left: 10px;
    display: flex;
    flex-direction: column;
}

.h2 {
    display: grid;
    grid-column: span 2;
}

.boton-otro {
    display: grid;
    background-color: gray;
    border-radius: 30px;
    color: white;
    width: 200px;
    height: 40px;
    margin-left: 20px;
    justify-content: center;
    align-items: center;
}

.boton-otro:hover {
    cursor: pointer;
    color: gray;
    background-color: white;
}

.cont1 {
    display: flex;
    height: 300px;
    width: 500px;
    margin-top: 50px;
    column-gap: 20px;
    padding-left: 40px;
    font-size: 30px;
}

.contactanos {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 80%;
    padding-top: 50px;
    column-gap: 10px;
    row-gap: 10px;
    padding-top: 20px;
}

.cuadritos-contact {
    background-color: gray;
    color: #fff;
    height: 50px;
    display: flex;
    align-items: center;
    padding-left: 10px;
}

.redes {
    background-color: gray;
    justify-content: space-between;
    display: flex;
    align-items: center;
    padding-left: 10px;
    color: #fff;
    width: 90%;
    padding-right: 20px;
}

.warning {
    color: red;
    background-color: lightcoral;
    width: 15%;
}

.success {
    color: green;
    background-color: lightgreen;
    width: 15%;
}

.inicio-nc {
    display: flex;
    flex-direction: column;
    height: 700px;
    width: 97%;
    padding-left: 50px;
    padding-top: 50px;
    align-items: center;
    justify-content: center;
}

.cuadritos-inp {
    height: 5%;
    width: 100%;
    border-radius: 50px;
    padding: 5px;
    gap: 30px;
}

/* Media Queries para Tablet y Móvil */
@media screen and (max-width:600px) {
    .header {
        height: 200px;
        margin-top: 20px;
        margin-right: 50px;
        padding-bottom: 8px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;

    }

    .cont1 {
        padding-left: 0;
        font-size: 20px;
        display: flex;
        flex-direction: column;
    }

    .menu {
        display: flex;
        gap: 20px;
        justify-content: center;
    }

    .mision {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-bottom: 80px;
        padding-left: 50px;
        height: auto;
    }

    .inicio {
        height: auto;
        width: 500px;
        padding-left: 50px;
        padding-top: 50px;
    }

    .separador {
        display: flex;
        flex-direction: column;
        height: auto;
        width: 99%;
        padding-top: 50px;
    }

    .img1 {
        width: 600px;
        height: 700px;
        grid-column-start: 2;
        grid-column-end: 3;
        margin-top: -100px;
        display: none;
    }

    .parrafo {
        font-size: 19px;
        width: 240px;
        height: 280px;

    }

    .sobre-nosotros {
        height: 170px;
        width: 90%;
        font-size: 30px;
        display: flex;
        justify-content: center;
        align-items: end;
        padding-left: 20px;
        padding-bottom: 30px;
        border-bottom: solid black 3px;
    }

    .actividades {
        height: auto;
        padding-left: 20px;
    }

    .acts {
        width: 500px;
        flex-direction: column;
        justify-content: start;
        row-gap: 50px;
        margin-right: 300px;
    }

    .cuadros {
        width: 55%;
    }

    .contenedor-galeria {
        display: flex;
        flex-direction: column;
        height: auto;
        justify-content: center;
        align-items: center;

    }

    .galeria {
        display: flex;
        flex-direction: column;
        grid-template-columns: 1fr;
        align-items: center;
        justify-content: center;
    }

    .galeria img {
        width: 100%;
        height: auto;
    }

    .galeria-inicio {
        height: 2300px;
        width: 97%;
        padding-left: 50px;
        padding-top: 50px
    }

    .footer {
        height: 700px;
        width: 97%;
        padding-left: 50px;
        padding-top: 50px
    }

    .inicio-nc {
        display: flex;
        flex-direction: column;
        height: 700px;
        width: 97%;
        padding-left: 50px;
        padding-top: 50px;
        align-items: center;
        justify-content: center;
    }

    .cuadritos-inp {
        height: 5%;
        width: 100%;
        border-radius: 50px;
        padding: 5px;
        gap: 30px;
    }
}
</style>
