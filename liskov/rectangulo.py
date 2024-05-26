from figura import Figura


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def perimetro(self):
        return (2 * self.base) + (2 * self.altura)

    def area(self):
        return self.base * self.altura