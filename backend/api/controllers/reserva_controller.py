from flask import Blueprint, request, jsonify
from models.reserva_model import Reserva

# Crear el blueprint del controlador
reserva_controller = Blueprint('reserva_controller', __name__)

# Ruta para crear una nueva reserva


@reserva_controller.route('/reservas', methods=['POST'])
def crear_reserva():
    # Obtener los datos de la reserva desde el cuerpo de la solicitud
    datos_reserva = request.get_json()

    # Validar los datos de la reserva

    # Crear una nueva instancia de la reserva
    nueva_reserva = Reserva(
        datos_reserva['nombre'], datos_reserva['correo'], datos_reserva['numero'])

    # Guardar la reserva en la base de datos
    nueva_reserva.guardar()

    # Devolver una respuesta exitosa
    return jsonify({'message': 'Reserva creada exitosamente'}), 201

# Ruta para obtener todas las reservas


@reserva_controller.route('/reservas', methods=['GET'])
def obtener_reservas():
    # Obtener todas las reservas de la base de datos
    reservas = Reserva.obtener_todas()

    # Crear una lista para almacenar los datos de las reservas
    datos_reservas = []

    # Recorrer las reservas y obtener sus datos
    for reserva in reservas:
        datos_reserva = {
            'id': reserva.id,
            'nombre': reserva.nombre,
            'correo': reserva.correo,
            'numero': reserva.numero
        }
        datos_reservas.append(datos_reserva)

    # Devolver los datos de las reservas en formato JSON
    return jsonify(datos_reservas), 200

# Ruta para obtener una reserva por su ID


@reserva_controller.route('/reservas/<int:id>', methods=['GET'])
def obtener_reserva(id):
    # Obtener la reserva por su ID desde la base de datos
    reserva = Reserva.obtener_por_id(id)

    # Verificar si la reserva existe
    if reserva is None:
        return jsonify({'message': 'Reserva no encontrada'}), 404

    # Devolver los datos de la reserva en formato JSON
    datos_reserva = {
        'id': reserva.id,
        'nombre': reserva.nombre,
        'correo': reserva.correo,
        'numero': reserva.numero
    }
    return jsonify(datos_reserva), 200

# Ruta para actualizar una reserva por su ID


@reserva_controller.route('/reservas/<int:id>', methods=['PUT'])
def actualizar_reserva(id):
    # Obtener los datos actualizados de la reserva desde el cuerpo de la solicitud
    datos_reserva = request.get_json()

    # Obtener la reserva por su ID desde la base de datos
    reserva = Reserva.obtener_por_id(id)

    # Verificar si la reserva existe
    if reserva is None:
        return jsonify({'message': 'Reserva no encontrada'}), 404

    # Actualizar los datos de la reserva
    reserva.nombre = datos_reserva['nombre']
    reserva.correo = datos_reserva['correo']
    reserva.numero = datos_reserva['numero']

    # Guardar los cambios en la base de datos
    reserva.guardar()

    # Devolver una respuesta exitosa
    return jsonify({'message': 'Reserva actualizada exitosamente'}), 200

# Ruta para eliminar una reserva por su ID


@reserva_controller.route('/reservas/<int:id>', methods=['DELETE'])
def eliminar_reserva(id):
    # Obtener la reserva por su ID desde la base de datos
    reserva = Reserva.obtener_por_id(id)

    # Verificar si la reserva existe
    if reserva is None:
        return jsonify({'message': 'Reserva no encontrada'}), 404

    # Eliminar la reserva de la base de datos
    reserva.eliminar()

    # Devolver una respuesta exitosa
    return jsonify({'message': 'Reserva eliminada exitosamente'}), 200
