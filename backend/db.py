import mysql.connector

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'carrizalesprueba.mysql.database.azure.com',
    'user': 'elmer',
    'password': 'Codex@01',
    'database': 'carrizalesprueba'
}

# Crear la conexión a la base de datos
connection = mysql.connector.connect(**db_config)

# Verificar si la conexión fue exitosa
if connection.is_connected():
    print('Conexión exitosa a la base de datos')

# Cerrar la conexión al finalizar la aplicación
def close_connection():
    if connection.is_connected():
        connection.close()
        print('Conexión cerrada')

