// JavaScript para la página

// Obtener la barra de navegación
const navbar = document.getElementById('navbar');
// Obtener el elemento del texto del logo
const logoText = document.querySelector('.logo-text');
// Obtener el elemento del logo grande
const logoGrande = document.querySelector('.logo-grande');

// Variables para el control de la animación
let lastScrollTop = 0;
let scrolling = false;

// Función para cambiar la apariencia de la barra de navegación al hacer scroll
function changeNavbarAppearance() {
    if (!scrolling) {
        window.requestAnimationFrame(function () {
            const scrollTop = window.scrollY;

            if (scrollTop > lastScrollTop) {
                // Hacer scroll hacia abajo
                navbar.classList.add('scrolled');
                logoText.style.visibility = 'visible';
                logoText.style.opacity = '1';
                logoGrande.style.opacity = '0';
            } else {
                // Hacer scroll hacia arriba
                navbar.classList.remove('scrolled');
                logoText.style.visibility = 'hidden';
                logoText.style.opacity = '0';
                logoGrande.style.opacity = '1';
            }

            lastScrollTop = scrollTop;
            scrolling = false;
        });

        scrolling = true;
    }
}

// Escuchar el evento de scroll y llamar a la función de cambio de apariencia
window.addEventListener('scroll', changeNavbarAppearance);
