class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
    def mudarCanal(self, novoCanal):
        if novoCanal <= 100 and novoCanal > 0:
            self.canal = novoCanal
        else:
            print('Canal inexistente')
    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print('Volume já está no mínimo!')
    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print('Valor já está no máximo!')

Televisor = TV(56, 2)
print(f'Canal: {Televisor.canal}, Volume: {Televisor.volume}')
Televisor.mudarCanal(12)
print(f'Canal: {Televisor.canal}, Volume: {Televisor.volume}')
Televisor.mudarCanal(123)
print(f'Canal: {Televisor.canal}, Volume: {Televisor.volume}')
Televisor.aumentarVolume()
print(f'Canal: {Televisor.canal}, Volume: {Televisor.volume}')
Televisor.diminuirVolume()
print(f'Canal: {Televisor.canal}, Volume: {Televisor.volume}')
Televisor.diminuirVolume()
print(f'Canal: {Televisor.canal}, Volume: {Televisor.volume}')
Televisor.diminuirVolume()
print(f'Canal: {Televisor.canal}, Volume: {Televisor.volume}')
Televisor.diminuirVolume()
print(f'Canal: {Televisor.canal}, Volume: {Televisor.volume}')






# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.