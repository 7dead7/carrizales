from flask import Blueprint, request, jsonify
from .controllers.reserva_controller import guardar_reserva

# Crear el Blueprint para las rutas del restaurante
restaurante_bp = Blueprint('restaurante', __name__)

# Ruta para recibir los datos del formulario de reserva
@restaurante_bp.route('/reservas', methods=['POST'])
def reservas():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    numero = request.form.get('numero')

    # Validar los datos del formulario

    # Guardar la reserva en la base de datos
    reserva_id = guardar_reserva(nombre, correo, numero)

    # Realizar otras acciones necesarias

    # Devolver una respuesta JSON
    return jsonify({'message': 'Reserva exitosa', 'reserva_id': reserva_id})

# Resto de las rutas y lógica del restaurante...

