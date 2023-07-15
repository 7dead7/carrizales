// JavaScript para la página de reservas

// Obtener el elemento del navbar
const navbar = document.getElementById('navbar');

// Cambiar el tamaño del navbar al hacer scroll
window.addEventListener('scroll', () => {
    if (window.scrollY > 0) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Función para desplegar el formulario al hacer clic en el estado de disponibilidad
function mostrarFormulario() {
    const mesa = this.parentElement;
    const formulario = mesa.querySelector('.formulario-container');
    formulario.classList.toggle('hide');
}

// Agregar el evento de clic a los estados de disponibilidad
const estadosDisponibilidad = document.querySelectorAll('.estado-disponible');
estadosDisponibilidad.forEach((estado) => {
    estado.addEventListener('click', mostrarFormulario);
});

// Función para mostrar el formulario de notificación de disponibilidad
function mostrarFormularioNotificacion() {
    const mesa = this.parentElement;
    const formulario = mesa.querySelector('.formulario-container');
    const reservaForm = formulario.querySelector('.reserva-form');
    const correoForm = formulario.querySelector('.correo-form');
    const mensajeNotificacion = formulario.querySelector('.mensaje-notificacion');

    reservaForm.classList.add('hide');
    correoForm.classList.remove('hide');
    mensajeNotificacion.classList.add('hide');

    formulario.classList.toggle('hide');
}

// Agregar el evento de clic al estado de no disponibilidad
const estadoNoDisponible = document.querySelector('.estado-no-disponible');
estadoNoDisponible.addEventListener('click', mostrarFormularioNotificacion);

// Función para cerrar el formulario
function cerrarFormulario() {
    const formulario = this.parentElement;
    formulario.classList.add('hide');
}

// Agregar el evento de clic al botón de cerrar formulario
const closeButtons = document.querySelectorAll('.close-button');
closeButtons.forEach((button) => {
    button.addEventListener('click', cerrarFormulario);
});

// Obtener los elementos del formulario de reserva
const reservaForm = document.querySelectorAll('.reserva-form');
const correoForm = document.querySelectorAll('.correo-form');

// Función para manejar el envío del formulario de reserva
function handleReservaSubmit(event) {
    event.preventDefault();

    // Obtener los valores de los campos del formulario
    const nombre = this.querySelector('#nombre').value;
    const correo = this.querySelector('#correo').value;
    const numero = this.querySelector('#numero').value;

    // Realizar acciones con los datos del formulario (enviar correo, guardar reserva, etc.)

    // Mostrar el mensaje de confirmación
    const mensajeConfirmacion = document.createElement('p');
    mensajeConfirmacion.textContent = 'Reserva confirmada';
    mensajeConfirmacion.classList.add('mensaje-confirmacion');
    this.insertAdjacentElement('afterend', mensajeConfirmacion);

    // Limpiar los campos del formulario
    this.reset();

    // Cerrar el formulario después de 2 segundos
    setTimeout(() => {
        mensajeConfirmacion.remove();
        const formulario = this.parentElement;
        formulario.classList.add('hide');
    }, 2000);
}

// Función para manejar el envío del formulario de notificación de disponibilidad
function handleNotificarSubmit(event) {
    event.preventDefault();

    // Obtener el correo ingresado
    const correo = this.querySelector('#correo').value;

    // Realizar acciones con el correo ingresado (enviar notificación, etc.)

    // Mostrar el mensaje de notificación
    const mensajeNotificacion = this.parentElement.querySelector('.mensaje-notificacion');
    mensajeNotificacion.classList.remove('hide');

    // Limpiar el campo del formulario
    this.reset();
}

// Escuchar el evento submit del formulario de reserva
reservaForm.forEach((form) => {
    form.addEventListener('submit', handleReservaSubmit);
});

// Escuchar el evento submit del formulario de notificación de disponibilidad
correoForm.forEach((form) => {
    form.addEventListener('submit', handleNotificarSubmit);
});
