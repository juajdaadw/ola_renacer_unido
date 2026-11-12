<template>
    <div class="pagina-beneficiario">

        <div class="contenedor-formulario">
            <div class="encabezado">
                <h2>REGISTRAR GUARDIAN</h2>
                <p>Ingrese los datos del habitante de calle para integrarlo al programa de guardianes.</p>
            </div>

            <div class="formulario">
                <label class="etiqueta" for="ben-nombre">Nombre Completo:</label>
                <input id="ben-nombre" v-model="habitante.nombre" type="text"
                    placeholder="Nombre del habitante de calle..." class="cajas-texto">

                <label class="etiqueta" for="ben-edad">Edad aproximada:</label>
                <input id="ben-edad" v-model.number="habitante.edad" type="number" class="cajas-texto">

                <label class="etiqueta" for="ben-zona">Zona de intervención asignada:</label>
                <select id="ben-zona" v-model="habitante.zona" class="cajas-texto">
                    <option :value="0">Seleccione zona...</option>
                    <option :value="1">Centro Histórico</option>
                    <option :value="2">El Rodadero</option>
                    <option :value="3">Taganga</option>
                </select>

                <label class="etiqueta" for="ben-obs">Observaciones médicas o sociales:</label>
                <textarea id="ben-obs" v-model="habitante.observaciones" rows="3" placeholder="Detalles importantes..."
                    class="cajas-texto"></textarea>

                <div v-if="exito" class="exito">{{ exito }}</div>
                <div v-if="advertencia" class="warning">{{ advertencia }}</div>

                <div class="zona-botones">
                    <button id="btn-cancelar" class="boton-form" @click="volver">Volver</button>
                    <button id="btn-guardar" :disabled="guardando" class="boton-form btn-verde" @click="guardar">
                        {{ guardando ? 'Guardando...' : 'Guardar Registro' }}
                    </button>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: 'RegistrarHabitanteView',
    data() {
        return {
            habitante: {
                nombre: '',
                edad: '',
                zona: 0,
                observaciones: ''
            },
            guardando: false,
            advertencia: '',
            exito: ''
        };
    },
    methods: {
        async guardar() {
            const h = this.habitante;

            if (h.nombre === '' || h.zona === 0) {
                this.advertencia = 'Complete los campos principales';
                this.exito = '';
                return;
            }

            this.advertencia = '';
            this.guardando = true;
            try {
                await this.axios.post('/beneficiarios', {
                    nombre: h.nombre,
                    edad: h.edad === '' ? null : h.edad,
                    zona: h.zona,
                    observaciones: h.observaciones
                }, { headers: { Authorization: 'Bearer ' + localStorage.getItem('token') } });
                this.exito = 'Beneficiario registrado correctamente';
                this.habitante = { nombre: '', edad: '', zona: 0, observaciones: '' };
            } catch (e) {
                console.log(e.message);
                this.exito = '';
                const estado = e.response ? e.response.status : null;
                if (estado === 401) {
                    localStorage.removeItem('token');
                    localStorage.removeItem('rol');
                    this.$router.push('/login');
                } else if (estado === 403) {
                    this.advertencia = 'No tienes permiso para registrar habitantes';
                } else {
                    this.advertencia = 'No se pudo guardar el registro. Intenta de nuevo';
                }
            } finally {
                this.guardando = false;
            }
        },

        volver() {
            this.$router.push('/home');
        }
    }
};
</script>

<style scoped>
.pagina-beneficiario {
    font-family: sans-serif;
    min-height: 100vh;
    display: flex;
    align-items: center;
}

.contenedor-formulario {
    width: 90%;
    max-width: 500px;
    margin: auto;
    background-color: white;
    border-radius: 25px;
    padding: 30px;
    box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.1);
}

.encabezado {
    text-align: center;
    margin-bottom: 20px;
}

.encabezado h2 {
    color: #3ca9d0;
    margin-bottom: 10px;
}

.etiqueta {
    display: block;
    margin-top: 15px;
    color: #555;
    font-weight: bold;
}

.cajas-texto {
    width: 100%;
    padding: 10px;
    border: 1px solid #6bc7e8;
    border-radius: 10px;
    margin-top: 5px;
    box-sizing: border-box;
}

.zona-botones {
    margin-top: 25px;
    display: flex;
    justify-content: space-between;
}

.boton-form {
    padding: 10px 20px;
    border-radius: 10px;
    cursor: pointer;
    border: none;
    font-weight: bold;
}

#btn-cancelar {
    background-color: gray;
    color: white;
}

.btn-verde {
    background-color: #2e7d32;
    color: white;
}

.exito {
    background-color: lightgreen;
    color: green;
    padding: 10px;
    border-radius: 10px;
    margin-top: 10px;
    text-align: center;
}

.warning {
    background-color: lightcoral;
    color: red;
    padding: 10px;
    border-radius: 10px;
    margin-top: 10px;
    text-align: center;
}
</style>
