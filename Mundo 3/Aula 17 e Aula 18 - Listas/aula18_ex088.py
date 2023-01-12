from random import randint
from time import sleep
jogo = []
quantos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-= SORTEANDO {quantos} JOGOS =-=-=')
for c in range(0, quantos):
    while True:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
        if len(jogo) == 6:
            break
    jogo.sort()
    print(f'Jogo {c+1}: {jogo}')
    sleep(1)
    jogo.clear()
print('-=-=-=-=- < BOA SORTE! > -=-=-=-=-')