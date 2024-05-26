class ManejadorDatos:
    def procesar(self, db, datos):
        db.guardar(datos)
        db.leer()
