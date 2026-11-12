<template>
    <div class="pagina-galeria">
        <header class="header">
            <div class="inicio" @click="volver">
                <img class="icon" src="../assets/home.svg" alt="Inicio">
                <h1>Inicio</h1>
            </div>

            <h1 class="op-galeria">GALERIA</h1>
        </header>

        <p v-if="errorApi" class="error-api">{{ errorApi }}</p>

        <main class="galeria">
            <template v-if="cargando">
                <div v-for="n in 7" :key="n" :class="'img' + n">
                    <SkeletonPrime width="100%" height="100%" borderRadius="0" />
                </div>
            </template>

            <template v-else>
                <div v-for="(foto, index) in galeria" :key="foto.id" :class="'img' + (index + 1)">
                    <img class="img" :src="foto.url" :alt="foto.alt">
                </div>
            </template>
        </main>
    </div>
</template>

<script>
export default {
    name: 'GaleriaView',
    data() {
        return {
            galeria: [],
            cargando: false,
            errorApi: ''
        };
    },
    methods: {
        async cargarGaleria() {
            this.cargando = true;
            this.errorApi = '';
            try {
                const { data } = await this.axios.get('/imagenes/galeria');
                this.galeria = data;
            } catch (e) {
                console.log(e);
                this.errorApi = 'No se pudo cargar la galería. Revisa que la API esté encendida e intenta de nuevo.';
            } finally {
                this.cargando = false;
            }
        },
        volver() {
            this.$router.push('/home');
        }
    },
    mounted() {
        this.cargarGaleria();
    }
};
</script>

<style scoped>
* {
    padding: 0%;
    box-sizing: border-box;
}

.pagina-galeria {
    min-height: 100vh;
    padding: 8px;
}

.header {
    display: flex;
    background-color: #57aecd;
    padding: 10px;
    align-items: center;
    justify-content: space-between;
}

.icon {
    height: 100px;
    width: 100px;
}

.img {
    width: 100%;
    height: 100%;
}

.inicio {
    font-size: 25px;
    color: #fff;
    display: flex;
}

.inicio:hover {
    cursor: pointer;
}

.op-galeria {
    margin-right: 45%;
    color: #fff;
}

.error-api {
    background-color: lightcoral;
    color: red;
    padding: 10px;
    text-align: center;
}

.galeria {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr;
    width: 100%;
    height: 85vh;
    row-gap: 3px;
    column-gap: 5px;
}

.img1 {
    grid-column-start: 1;
    grid-column-end: 2;
    grid-row-start: 1;
    grid-row-end: 3;
}

.img2 {
    grid-column-start: 2;
    grid-column-end: 3;
    grid-row-start: 1;
    grid-row-end: 2;
}

.img3 {
    grid-column-start: 3;
    grid-column-end: 4;
    grid-row-start: 1;
    grid-row-end: 2;
}

.img4 {
    grid-column-start: 4;
    grid-column-end: 5;
    grid-row-start: 1;
    grid-row-end: 3;
}

.img5 {
    grid-column-start: 1;
    grid-column-end: 2;
    grid-row-start: 3;
    grid-row-end: 4;
}

.img6 {
    grid-column-start: 2;
    grid-column-end: 4;
    grid-row-start: 2;
    grid-row-end: 4;
}

.img7 {
    grid-column-start: 4;
    grid-column-end: 5;
    grid-row-start: 3;
    grid-row-end: 4;
}
</style>
