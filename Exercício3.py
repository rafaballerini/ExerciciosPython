class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    def mudarValores(self, ladoA2, ladoB2):
        self.ladoA = ladoA2
        self.ladoB = ladoB2
    def retornarValores(self):
        print(self.ladoA, self.ladoB)
    def calcularArea(self):
        area = self.ladoA * self.ladoB
        return area
    def calcularPerimetro(self):
        perimetro = (self.ladoA*2) + (self.ladoB *2)
        return perimetro


lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
retangulozi = Retangulo(ladoA=lado1, ladoB=lado2)
print(retangulozi.calcularArea(), ' de peças')
print(retangulozi.calcularPerimetro(), ' de rodapé')
retangulozi.mudarValores(ladoA2=8, ladoB2=2)