from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
ranking = []
print('** JOGO DE DADOS **')
n = int(input('Quantos jogadores? '))
for c in range(1, n+1):
    jogadores[f'Jogador_{c}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'{k} tirou: {v}')
    sleep(1)
print('=-'*20)

print(' == RANKING == ')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")
    sleep(0.5)
