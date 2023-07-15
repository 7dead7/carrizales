from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar CORS
CORS(app)

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'carrizalesprueba.mysql.database.azure.com',
    'user': 'elmer',
    'password': 'Codex@01',
    'database': 'carrizalesprueba'
}

# Crear la conexión a la base de datos
db_connection = mysql.connector.connect(**db_config)
db_cursor = db_connection.cursor()


# Ruta para recibir los datos del formulario de reserva
@app.route('/reservas', methods=['POST'])
def add_reserva():
    # Obtener los datos del formulario
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    numero = request.form.get('numero')

    # Validar los campos requeridos
    if not nombre or not correo or not numero:
        return jsonify({'error': 'Todos los campos son requeridos'}), 400

    # Insertar los datos en la base de datos
    query = 'INSERT INTO reservas (nombre, correo, numero) VALUES (%s, %s, %s)'
    values = (nombre, correo, numero)
    db_cursor.execute(query, values)
    db_connection.commit()

    return jsonify({'message': 'Reserva exitosa'}), 200


# Ruta para obtener todas las reservas
@app.route('/reservas', methods=['GET'])
def get_reservas():
    # Obtener todas las reservas de la base de datos
    query = 'SELECT * FROM reservas'
    db_cursor.execute(query)
    rows = db_cursor.fetchall()

    # Convertir los resultados a un formato JSON
    reservas = []
    for row in rows:
        reserva = {
            'id': row[0],
            'nombre': row[1],
            'correo': row[2],
            'numero': row[3]
        }
        reservas.append(reserva)

    return jsonify(reservas), 200


if __name__ == '__main__':
    app.run()
