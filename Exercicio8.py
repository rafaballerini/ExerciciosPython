class Macaco:
    def __init__(self, nome):
        self.nome  = nome
        self.bucho = []
    def comer(self, alimento):
        self.bucho.append(alimento)
    def verBucho(self):
        return self.bucho
    def digerir(self):
        self.bucho.clear()

primeiroNome = input('Digite o nome do primeiro macaco: ')
segundoNome  = input('Digite o nome do segundo macaco: ')
primeiroMacaco = Macaco(nome = primeiroNome)
segundoMacaco  = Macaco(nome = segundoNome)
alimento1 = input(f'Qual alimento deseja dar ao macaco {primeiroMacaco.nome}? ')
alimento2 = input(f'Qual alimento deseja dar ao macaco {segundoMacaco.nome}? ')
primeiroMacaco.comer(alimento1)
segundoMacaco.comer(alimento2)
print(F'Bucho do macaco 1: ', primeiroMacaco.verBucho())
print(f'Bucho do macaco 2: ', segundoMacaco.verBucho())
alimento1 = input(f'Qual alimento deseja dar ao macaco {primeiroMacaco.nome}? ')
alimento2 = input(f'Qual alimento deseja dar ao macaco {segundoMacaco.nome}? ')
primeiroMacaco.comer(alimento1)
segundoMacaco.comer(alimento2)
print(F'Bucho do macaco {primeiroMacaco.nome}: ', primeiroMacaco.verBucho())
print(f'Bucho do macaco {segundoMacaco.nome}: ', segundoMacaco.verBucho())
alimento1 = input(f'Qual alimento deseja dar ao macaco {primeiroMacaco.nome}? ')
alimento2 = input(f'Qual alimento deseja dar ao macaco {segundoMacaco.nome}? ')
primeiroMacaco.comer(alimento1)
segundoMacaco.comer(alimento2)
print(F'Bucho do macaco {primeiroMacaco.nome}: ', primeiroMacaco.verBucho())
print(f'Bucho do macaco {segundoMacaco.nome}: ', segundoMacaco.verBucho())
primeiroMacaco.digerir()
segundoMacaco.digerir()
print(F'Bucho do macaco {primeiroMacaco.nome}: ', primeiroMacaco.verBucho())
print(f'Bucho do macaco {segundoMacaco.nome}: ', segundoMacaco.verBucho())

