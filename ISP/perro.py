from carnivoro import Carnivoro


class Perro(Carnivoro):
    def respirar(self):
        return "perro, respirando"

    def comer(self):
        return "perro, comiendo"

    def dormir(self):
        return "perro, durmiendo"

    def cazar(self):
        return "perro, cazando"
