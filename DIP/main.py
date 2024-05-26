from mysql_db import MySQLDB
from mongodb import MongoDB
from manejador_datos import ManejadorDatos


data = {
    "nombre": "Dario",
    "telefono": "3001234567"
}

mongodb_base = MongoDB()
mysql_base = MySQLDB()
manejador = ManejadorDatos()
manejador.procesar(mongodb_base, data)
manejador.procesar(mysql_base, data)