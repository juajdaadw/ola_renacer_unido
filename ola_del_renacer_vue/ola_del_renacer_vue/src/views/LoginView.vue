<template>
    <div class="pagina-login" :style="estiloFondo">
        <div class="contenedor">
            <div class="blanco">
                <h1 class="iniciar-h1">Inicio de sesión</h1>
                <div class="casillas">
                    <h3>Usuario</h3>
                    <input v-model="credenciales.usuario" class="usuario" placeholder="Nombre de usuario"
                        @keyup.enter="iniciarSesion">
                    <h3>Contraseña</h3>
                    <input v-model="credenciales.contrasena" class="contraseña" placeholder="Contraseña" type="password"
                        @keyup.enter="iniciarSesion">
                    <button class="boton" :disabled="cargando" @click="iniciarSesion">
                        {{ cargando ? 'Ingresando...' : 'Iniciar sesion' }}
                    </button>

                    <div v-if="mensaje" class="msg">{{ mensaje }}</div>
                </div>
            </div>
            <div class="columna-imagen">
                <SkeletonPrime v-if="cargandoImagen" width="28rem" height="100%" borderRadius="25px" />
                <img v-else-if="imagen" id="img-login" class="verde" :src="imagen" alt="Imagen de una playa">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'LoginView',
    data() {
        return {
            credenciales: {
                usuario: '',
                contrasena: ''
            },
            mensaje: '',
            cargando: false,
            imagen: '',
            cargandoImagen: false
        };
    },
    computed: {
        estiloFondo() {
            return this.imagen ? { '--fondo-login': `url("${this.imagen}")` } : {};
        }
    },
    methods: {
        async cargarImagen() {
            this.cargandoImagen = true;
            try {
                const { data } = await this.axios.get('/imagenes/login');
                this.imagen = data[0].url;
            } catch (e) {
                console.log(e);
            } finally {
                this.cargandoImagen = false;
            }
        },

        async iniciarSesion() {
            if (this.credenciales.usuario === '' || this.credenciales.contrasena === '') {
                this.mensaje = 'No deje campos vacios';
                return;
            }

            this.cargando = true;
            this.mensaje = '';
            try {
                const { data } = await this.axios.post('/login', {
                    usuario: this.credenciales.usuario,
                    contrasena: this.credenciales.contrasena
                });

                if (data.status) {
                    localStorage.setItem('rol', data.rol);
                    this.$router.push('/home');
                } else {
                    this.mensaje = data.mensaje;
                }
            } catch (e) {
                console.log(e);
                this.mensaje = 'No se pudo conectar con el servidor';
            } finally {
                this.cargando = false;
            }
        }
    },
    mounted() {
        this.cargarImagen();
    }
};
</script>

<style scoped>
* {
    padding: 0%;
    box-sizing: border-box;
}

.pagina-login {
    min-height: 100vh;
    padding: 8px;
}

.contenedor {
    display: flex;
    flex-direction: row;
    background-color: white;
    opacity: 90%;
    width: 60%;
    height: 71.2vh;
    margin-left: 20%;
    margin-top: 100px;
    border-radius: 25px;
}

.msg {
    background-color: lightcoral;
    color: red;
    margin-top: 1rem;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 1.6rem;
    border-radius: 30px;
}

.boton {
    background-color: #6bc7e8;
    margin-top: 1.6rem;
    border-radius: 30px;
    width: 100%;
    height: 2rem;
}

.boton:hover {
    cursor: pointer;
    background-color: #559db7;
}

.verde {
    display: flex;
    width: 100%;
    height: 100%;
    border-radius: 25px;
}

.blanco {
    display: flex;
    flex-direction: column;
    justify-items: center;
    justify-content: center;
    width: 50%;
    padding-top: 5%;
    padding-left: 200px;
    margin-right: 125px;
    margin-left: -100px;
}

.casillas {
    display: grid;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-bottom: 200px;
    width: 300px;
    height: 200px;

}

.test {
    border: red 2px solid;
}

.usuario {
    display: grid;
    border-radius: 5px;
    height: 50px;
    justify-content: start;
    padding: 10px;
    align-items: center;
    width: 250px;
    background-color: #6bc7e8;
    border-color: white;
    border-radius: 30px;
}

.contraseña {
    display: grid;
    border-radius: 5px;
    height: 50px;
    justify-content: start;
    padding: 10px;
    align-items: center;
    width: 250px;
    background-color: #6bc7e8;
    border-color: white;
    border-radius: 30px;
}

.iniciar {
    display: grid;
    border-radius: 5px;
    height: 50px;
    justify-content: center;
    align-items: center;
    width: 250px;
    background-color: green;
    color: white;
}

.iniciar:hover {
    background-color: white;
    color: rgb(0, 0, 0);
    border: black solid 2px;
}

.iniciar-h1 {
    width: 300px;
}

@media screen and (max-width:777px) {

    .columna-imagen,
    #img-login {
        display: none;
    }

    .blanco {
        padding-left: 170px;
    }

    .usuario {
        width: 360px;
    }

    .contraseña {
        width: 360px;
    }

    .pagina-login {
        background-image: var(--fondo-login, linear-gradient(#6bc7e8, rgb(255, 255, 255)));
        background-size: cover;
    }

    .contenedor {
        opacity: 100%;
    }
}
</style>
