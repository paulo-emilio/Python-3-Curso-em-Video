import random

n = random.randint(1, 10)
jogador_num = 0
cont = 0
#print(n)

while n != jogador_num:
    jogador_num = int(input('Adivinhe o número: '))
    cont += 1
print(f'Parabéns, você só demorou {cont} tentativas para adivinhar')
