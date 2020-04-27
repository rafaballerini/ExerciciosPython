class ContaCorrente:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.saldo = 0.0
    def alterarNome(self, novoNome):
        self.nome = novoNome
    def deposito(self, valorDep):
        self.saldo += valorDep
    def saque(self, valorSaq):
        if self.saldo >= valorSaq:
            self.saldo -= valorSaq
        else:
            print('Não é possível sacar um valor maior que o saldo')

NovaConta = ContaCorrente(numero = '12345', nome = 'Rafaella')
print(f'Numero: {NovaConta.numero}, Nome: {NovaConta.nome}, Saldo: {round(NovaConta.saldo,2)}')
NovaConta.alterarNome('Matheus')
print(f'Numero: {NovaConta.numero}, Nome: {NovaConta.nome}, Saldo: {round(NovaConta.saldo,2)}')
NovaConta.deposito(100.50)
print(f'Numero: {NovaConta.numero}, Nome: {NovaConta.nome}, Saldo: {round(NovaConta.saldo,2)}')
NovaConta.saque(50.25)
print(f'Numero: {NovaConta.numero}, Nome: {NovaConta.nome}, Saldo: {round(NovaConta.saldo,2)}')
NovaConta.saque(50.50)
print(f'Numero: {NovaConta.numero}, Nome: {NovaConta.nome}, Saldo: {round(NovaConta.saldo,2)}')