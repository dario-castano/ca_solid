from herbivoro import Herviboro


class Vaca(Herviboro):
    def respirar(self):
        return "vaca, respirando"

    def comer(self):
        return "vaca, comiendo"

    def dormir(self):
        return "vaca, durmiendo"

    def pastar(self):
        return "vaca, pastando"
