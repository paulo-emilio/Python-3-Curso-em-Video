from random import randint
numeros = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(n, end=' - ')
print(f'\nMenor número: {min(numeros)}')
print(f'Maior número: {max(numeros)}')
