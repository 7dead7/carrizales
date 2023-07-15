from db import db


class Reserva:
    def __init__(self, nombre, correo, numero):
        self.nombre = nombre
        self.correo = correo
        self.numero = numero

    def guardar(self):
        try:
            query = "INSERT INTO reservas (nombre, correo, numero) VALUES (%s, %s, %s)"
            values = (self.nombre, self.correo, self.numero)
            db.execute(query, values)
            db.commit()
            return True
        except Exception as e:
            print("Error al guardar la reserva:", str(e))
            return False

    @staticmethod
    def obtener_todas():
        try:
            query = "SELECT * FROM reservas"
            result = db.execute(query)
            return result.fetchall()
        except Exception as e:
            print("Error al obtener las reservas:", str(e))
            return []

    @staticmethod
    def obtener_por_id(id):
        try:
            query = "SELECT * FROM reservas WHERE id = %s"
            values = (id,)
            result = db.execute(query, values)
            return result.fetchone()
        except Exception as e:
            print("Error al obtener la reserva:", str(e))
            return None

    @staticmethod
    def eliminar(id):
        try:
            query = "DELETE FROM reservas WHERE id = %s"
            values = (id,)
            db.execute(query, values)
            db.commit()
            return True
        except Exception as e:
            print("Error al eliminar la reserva:", str(e))
            return False
