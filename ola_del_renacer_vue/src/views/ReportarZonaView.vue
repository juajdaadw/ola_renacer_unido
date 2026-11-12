<template>
    <div class="pagina-zona">
        <div class="contenedor-formulario">

            <div class="encabezado">
                <h2>REPORTAR ZONA SUCIA</h2>
                <p>Ayúdanos a identificar los puntos críticos de Santa Marta para intervenir con nuestros guardianes.
                </p>
            </div>

            <div class="formulario">

                <label class="etiqueta" for="rep-nombre">Tu Nombre Completo:</label>
                <input id="rep-nombre" v-model="reporte.nombre" type="text" placeholder=" Digite su nombre..."
                    class="cajas-texto">

                <label class="etiqueta" for="rep-correo">Correo Electrónico:</label>
                <input id="rep-correo" v-model="reporte.correo" type="text" placeholder=" Ejemplo: juan@correo.com"
                    class="cajas-texto">

                <label class="etiqueta" for="rep-zona">Sector o Barrio de la Ciudad:</label>
                <select id="rep-zona" v-model="reporte.zona" class="cajas-texto">
                    <option :value="0">Seleccione la ubicación...</option>
                    <option :value="1">Centro Histórico</option>
                    <option :value="2">El Rodadero</option>
                    <option :value="3">Taganga</option>
                    <option :value="4">Bello Horizonte</option>
                    <option :value="5">Mamatoco</option>
                    <option :value="6">Otro sector</option>
                </select>

                <label class="etiqueta" for="rep-direccion">Dirección o Referencia Exacta:</label>
                <input id="rep-direccion" v-model="reporte.direccion" type="text"
                    placeholder=" Ejemplo: Calle 15 con Carrera 3" class="cajas-texto">

                <label class="etiqueta" for="rep-descripcion">Descripción del Estado de la Zona:</label>
                <textarea id="rep-descripcion" v-model="reporte.descripcion" rows="4"
                    placeholder=" Describa el problema (basura acumulada, escombros...)"
                    class="cajas-texto"></textarea>

                <div v-if="exito" class="exito">{{ exito }}</div>
                <div v-if="advertencia" class="warning">{{ advertencia }}</div>

                <div class="zona-botones">
                    <button id="btn-cancelar" class="boton-form" @click="volver">Volver</button>
                    <button id="btn-enviar" :disabled="enviando" class="boton-form btn-verde"
                        @click="validarReporte">
                        {{ enviando ? 'Enviando...' : 'Enviar Reporte' }}
                    </button>
                </div>

            </div>

        </div>
    </div>
</template>

<script>
export default {
    name: 'ReportarZonaView',
    data() {
        return {
            reporte: {
                nombre: '',
                correo: '',
                zona: 0,
                direccion: '',
                descripcion: ''
            },
            enviando: false,
            advertencia: '',
            exito: ''
        };
    },
    methods: {
        async validarReporte() {
            const r = this.reporte;
            this.exito = '';

            if (r.nombre === '') {
                this.advertencia = 'Por favor digite su nombre';
                return;
            }
            if (r.correo === '') {
                this.advertencia = 'Por favor digite su correo';
                return;
            }
            if (r.zona === 0) {
                this.advertencia = 'Por favor seleccione un sector';
                return;
            }
            if (r.direccion === '') {
                this.advertencia = 'Por favor ingrese una dirección de referencia';
                return;
            }
            if (r.descripcion === '') {
                this.advertencia = 'Por favor describa la situación de la zona';
                return;
            }

            this.advertencia = '';
            this.enviando = true;
            try {
                await this.axios.post('/reportes', {
                    nombre: r.nombre,
                    correo: r.correo,
                    zona: r.zona,
                    direccion: r.direccion,
                    descripcion: r.descripcion
                });
                this.exito = '¡Reporte enviado con éxito! Gracias por cuidar la ciudad.';
                this.limpiarCajas();
            } catch (e) {
                console.log(e);
                this.advertencia = 'No se pudo enviar el reporte. Intenta de nuevo';
            } finally {
                this.enviando = false;
            }
        },

        limpiarCajas() {
            this.reporte = { nombre: '', correo: '', zona: 0, direccion: '', descripcion: '' };
        },

        volver() {
            this.$router.push('/home');
        }
    }
};
</script>

<style scoped>
.pagina-zona {
    background-color: transparent;
    font-family: Arial, sans-serif;
    min-height: 100vh;
    display: flow-root;
}

.contenedor-formulario {
    width: 80%;
    max-width: 550px;
    margin: 50px auto;
    background-color: #ffffff;
    border: solid #6bc7e8 3px;
    border-radius: 10px;
    padding: 30px;
}

.encabezado {
    text-align: center;
    margin-bottom: 25px;
}

.encabezado h2 {
    color: #3ca9d0;
    margin-bottom: 5px;
}

.encabezado p {
    color: #555555;
    font-size: 14px;
}

.etiqueta {
    display: block;
    margin-top: 15px;
    margin-bottom: 5px;
    color: #555555;
    font-weight: bold;
    font-size: 14px;
}

.cajas-texto {
    width: 100%;
    padding: 10px;
    border: solid #6bc7e8 2px;
    border-radius: 5px;
    box-sizing: border-box;
    font-size: 14px;
    background-color: #ffffff;
}

.warning {
    background-color: lightcoral;
    color: red;
    padding: 10px;
    margin-top: 15px;
    border-radius: 5px;
    text-align: center;
    font-weight: bold;
}

.exito {
    background-color: lightgreen;
    color: green;
    padding: 10px;
    margin-top: 15px;
    border-radius: 5px;
    text-align: center;
    font-weight: bold;
}

.zona-botones {
    margin-top: 25px;
    text-align: center;
}

.boton-form {
    width: 45%;
    padding: 12px;
    font-size: 14px;
    font-weight: bold;
    cursor: pointer;
    border-radius: 5px;
    border: none;
    margin: 0 5px;
}

#btn-cancelar {
    background-color: gray;
    color: white;
}

.btn-verde {
    background-color: #2e7d32;
    color: white;
}

.btn-verde:hover {
    background-color: #1b5e20;
}

#btn-cancelar:hover {
    background-color: dimgray;
}
</style>
