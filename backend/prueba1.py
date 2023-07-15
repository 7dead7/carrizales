import mysql.connector

# Realizar la conexión a la base de datos
db_config = {
    'host': 'carrizalesprueba.mysql.database.azure.com',
    'user': 'elmer',
    'password': 'Codex@01',
    'database': 'carrizalesprueba',
}

# Establecer la conexión
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Realizar la consulta para recuperar los registros
query = "SELECT * FROM reservas"
cursor.execute(query)
result = cursor.fetchall()

# Mostrar los registros obtenidos
for row in result:
    print(row)

# Cerrar la conexión
cursor.close()
connection.close()
