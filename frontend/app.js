document.getElementById('reservaForm').addEventListener('submit', function (event) {
    event.preventDefault();

    // Obtener los valores de los campos del formulario
    const nombre = document.getElementById('nombre').value;
    const correo = document.getElementById('correo').value;
    const numero = document.getElementById('numero').value;

    // Crear el objeto de datos a enviar al servidor
    const reservaData = {
        nombre: nombre,
        correo: correo,
        numero: numero
    };

    // Realizar la solicitud al servidor para guardar la reserva
    fetch('http://localhost:5000/reservas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(reservaData)
    })
        .then(response => {
            if (response.ok) {
                console.log('Reserva guardada correctamente');
            } else {
                console.error('Error al guardar la reserva');
            }
        })
        .catch(error => {
            console.error('Error al enviar los datos:', error);
        });
});
