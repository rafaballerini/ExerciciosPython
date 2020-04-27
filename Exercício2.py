class Quadrado:
    def __init__(self, tamanhoDoLado):
        self.tamanhoDoLado = tamanhoDoLado
    def mudarValorDoLado(self, tamanhoNovo):
        self.tamanhoDoLado = tamanhoNovo
    def retornarValorLado(self):
        print(self.tamanhoDoLado)
    def calcularArea(self):
        area = self.tamanhoDoLado * self.tamanhoDoLado
        return area


quadradinho = Quadrado(tamanhoDoLado='4')
quadradinho.retornarValorLado()
quadradinho.mudarValorDoLado(10)
quadradinho.retornarValorLado()
print(quadradinho.calcularArea())
