"""
if carro.esquerda():
    bloco True
else:
    bloco False
"""
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro Novo! :)')
else:
    print('Carro Velho :(')
print('___FIM___')

tempo = int(input('Quantos anos tem sua Moto? '))
print('Moto Nova! :)' if tempo <= 3 else 'Moto velha :(')
