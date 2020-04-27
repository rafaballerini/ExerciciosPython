class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self):
        self.idade += 1
    def engordar(self):
        self.peso += 1
    def emagrecer(self):
        self.peso -= 1
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.5

Rafaella = Pessoa(nome = 'Rafaella', idade = 10, peso = 70.0, altura = 1.78)
print(f'Nome: {Rafaella.nome}, Idade: {Rafaella.idade}, Peso: {Rafaella.peso}, Altura: {Rafaella.altura}')
while Rafaella.idade < 80:
    Rafaella.envelhecer()
    Rafaella.engordar()
    Rafaella.emagrecer()
    Rafaella.crescer()
    print(f'Nome: {Rafaella.nome}, Idade: {Rafaella.idade}, Peso: {Rafaella.peso}, Altura: {round(Rafaella.altura,2)}')


