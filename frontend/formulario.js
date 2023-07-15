// JavaScript para el formulario de reservas
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('reserva-form');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        alert('Gracias por tu reserva. Serás notificado cuando haya lugares disponibles.');
        form.reset();
    });
});
