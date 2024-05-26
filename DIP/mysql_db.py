from base_datos import BaseDatos
import mysql.connector


class MySQLDB(BaseDatos):
    def __init__(self):
        self.config = {
            'user': 'dario',
            'password': 'pass',
            'host': '127.0.0.1',
            'database': 'default',
            'raise_on_warnings': True
        }
        self.connection = mysql.connector.connect(**self.config)

    def guardar(self, datos):
        nombre = datos.nombre
        telefono = datos.telefono

        query = f"INSERT INTO default (nombre, telefono) VALUES ({nombre}, {telefono})"

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def leer(self):
        query = f"SELECT * FROM default"

        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        for elem in result:
            print(elem)

        cursor.close()
