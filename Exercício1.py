class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def trocaCor(self, outraCor):
        self.cor = outraCor
    def mostraCor(self):
        print(self.cor)


bola1 = Bola(cor='azul', circunferencia='34', material='plastico')
bola1.mostraCor()
bola1.trocaCor('vermelho')
bola1.mostraCor()