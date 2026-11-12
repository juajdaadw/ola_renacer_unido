<template>
    <section class="banner-container" aria-roledescription="carousel" aria-label="Galería de imágenes destacadas"
        @mouseenter="pauseAutoplay" @mouseleave="startAutoplay">

        <!-- Mientras llegan las imágenes de la API -->
        <SkeletonPrime v-if="cargando" width="100%" height="100%" borderRadius="0" />

        <template v-else>
            <!-- Contenedor con overflow oculto -->
            <div class="carousel-viewport">
                <!-- Pista que se desplaza -->
                <div class="carousel-track" :style="trackStyle" @transitionend="handleTransitionEnd">
                    <figure v-for="(imgSrc, index) in displaySlides" :key="`${imgSrc}-${index}`" class="carousel-slide">
                        <img :src="imgSrc" alt="Playa de Santa Marta" />
                    </figure>
                </div>
            </div>

            <!-- Botón anterior (Izquierda) -->
            <button v-show="slides.length > 1" type="button" class="carousel-control prev" @click="prevSlide"
                aria-label="Imagen anterior">
                &#10094;
            </button>

            <!-- Botón siguiente (Derecha) -->
            <button v-show="slides.length > 1" type="button" class="carousel-control next" @click="nextSlide"
                aria-label="Imagen siguiente">
                &#10095;
            </button>

            <!-- Puntitos del slider -->
            <div v-show="slides.length > 1" class="slider-puntos">
                <span v-for="(slide, i) in slides" :key="i" class="punto" :class="{ active: i === indiceReal }"
                    @click="irASlide(i)"></span>
            </div>
        </template>
    </section>
</template>

<script>
export default {
    name: 'CarruselComponent',
    props: {
        // URLs de las imágenes (llegan desde la API)
        slides: {
            type: Array,
            default: () => []
        },
        // true mientras la API no ha respondido
        cargando: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            // Iniciamos en 1 debido al clon del último elemento al inicio
            currentIndex: 1,
            isTransitioning: true,
            autoplayTimer: null,
            transitionDuration: 500 // ms
        };
    },
    computed: {
        // Genera el arreglo con clones para el loop infinito: [Último, ...slides, Primero]
        displaySlides() {
            if (!this.slides || this.slides.length === 0) return [];
            if (this.slides.length === 1) return this.slides;

            const firstClone = this.slides[0];
            const lastClone = this.slides[this.slides.length - 1];
            return [lastClone, ...this.slides, firstClone];
        },
        // Posición real de la pista (con una sola imagen no hay clones, así que se queda en 0)
        posicion() {
            return this.slides.length > 1 ? this.currentIndex : 0;
        },
        // Estilos reactivos aplicados al track
        trackStyle() {
            return {
                transform: `translateX(-${this.posicion * 100}%)`,
                transition: this.isTransitioning
                    ? `transform ${this.transitionDuration}ms ease-in-out`
                    : 'none'
            };
        },
        // Cuál puntito se marca como activo (convierte la posición con clones a la imagen real)
        indiceReal() {
            const total = this.slides.length;
            if (total <= 1) return 0;
            if (this.currentIndex === 0) return total - 1;
            if (this.currentIndex === total + 1) return 0;
            return this.currentIndex - 1;
        }
    },
    watch: {
        // Las imágenes llegan después de montar el componente (vienen de la API),
        // así que cuando cambian reiniciamos la posición y el autoplay
        slides() {
            this.currentIndex = 1;
            this.isTransitioning = true;
            this.startAutoplay();
        }
    },
    methods: {
        nextSlide() {
            if (this.slides.length <= 1) return;
            this.isTransitioning = true;
            this.currentIndex++;
        },
        prevSlide() {
            if (this.slides.length <= 1) return;
            this.isTransitioning = true;
            this.currentIndex--;
        },
        // Click en un puntito: +1 porque la posición 0 es el clon del último
        irASlide(i) {
            if (this.slides.length <= 1) return;
            this.isTransitioning = true;
            this.currentIndex = i + 1;
        },

        handleTransitionEnd() {
            // Si llega al clon final, salta instantáneamente al primer slide real
            if (this.currentIndex === this.displaySlides.length - 1) {
                this.isTransitioning = false;
                this.currentIndex = 1;
            }
            // Si llega al clon inicial, salta instantáneamente al último slide real
            if (this.currentIndex === 0) {
                this.isTransitioning = false;
                this.currentIndex = this.displaySlides.length - 2;
            }
        },

        startAutoplay() {
            if (this.slides.length <= 1) return;
            this.clearAutoplay();
            this.autoplayTimer = setInterval(() => {
                this.nextSlide();
            }, 4000);
        },
        pauseAutoplay() {
            this.clearAutoplay();
        },
        clearAutoplay() {
            if (this.autoplayTimer) {
                clearInterval(this.autoplayTimer);
                this.autoplayTimer = null;
            }
        }
    },
    mounted() {
        this.startAutoplay();
    },
    beforeUnmount() {
        this.clearAutoplay();
    }
};
</script>

<style scoped>
.banner-container {
    position: relative;
    width: 100%;
    height: 500px;
    overflow: hidden;
    user-select: none;
    background-color: #000;
}

.carousel-viewport {
    width: 100%;
    height: 100%;
    overflow: hidden;
}

.carousel-track {
    display: flex;
    width: 100%;
    height: 100%;
    will-change: transform;
}

.carousel-slide {
    flex: 0 0 100%;
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
}

.carousel-slide img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    pointer-events: none;
}

/* Controles de navegación */
.carousel-control {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color: rgba(0, 0, 0, 0.45);
    color: #ffffff;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    z-index: 10;
    transition: background-color 0.3s ease, transform 0.2s ease;
}

.carousel-control:hover {
    background-color: rgba(0, 0, 0, 0.8);
    transform: translateY(-50%) scale(1.08);
}

.carousel-control:focus-visible {
    outline: 2px solid #ffffff;
}

.carousel-control.prev {
    left: 15px;
}

.carousel-control.next {
    right: 15px;
}

/* Puntitos del slider */
.slider-puntos {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 10px;
    z-index: 10;
}

.punto {
    width: 12px;
    height: 12px;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 50%;
    cursor: pointer;
    border: 1px solid rgba(0, 0, 0, 0.3);
}

.punto.active {
    background-color: white;
    transform: scale(1.2);
}

/* Media Queries para Tablet y Móvil */
@media (max-width: 768px) {
    .banner-container {
        height: 360px;
    }

    .carousel-control {
        width: 42px;
        height: 42px;
        font-size: 20px;
    }
}

@media (max-width: 576px) {
    .banner-container {
        height: 260px;
    }

    .carousel-control {
        width: 36px;
        height: 36px;
        font-size: 16px;
    }

    .carousel-control.prev {
        left: 8px;
    }

    .carousel-control.next {
        right: 8px;
    }
}
</style>
