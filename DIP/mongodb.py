from base_datos import BaseDatos
from pymongo import MongoClient


class MongoDB(BaseDatos):
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client["default"]
        self.coll = self.db["default"]

    def guardar(self, datos):
        self.coll.insert_one(datos)

    def leer(self):
        cursor = self.coll.find({})
        for document in cursor:
            print(document)
