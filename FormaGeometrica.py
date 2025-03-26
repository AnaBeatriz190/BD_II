import math

class FiguraGeometrica:
    def calcular_perimetro(self):
        raise NotImplementedError('Subclasse devem implementar este método')
class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio
    def calcular_perimetro(self):
        return math.pi * self.raio ** 2
class Retangulo(FiguraGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def calcular_perimetro(self):
        return self.largura * self.altura
        
        