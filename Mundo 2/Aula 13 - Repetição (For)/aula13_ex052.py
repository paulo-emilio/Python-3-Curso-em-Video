# Meu jeito:
n = int(input('Digite um número para descobrir se ele é primo: '))
cont = 0
d = 0

print('\nDivisões:', end=' ')

for c in range(n, 0, -1):
    if n % c == 0:
        print(c, end='. ')
        cont = cont + 1

print('\n')
if cont == 2:
    print(f'O número {n} foi divisível {cont} vezes. Ele é Primo.')
else:
    print(f'O número {n} foi divísvel {cont} vezes, ele NÃO é primo.')

print('\n\nGuanabara:')

# Guanabara jeito:
num = int(input('Digite um número: '))
contador = 0

for l in range(1, num + 1):  # (Número digitado) +1 para poder contar com ele
    if num % l == 0:
        print('\033[34m', end='')
        contador = contador + 1
    else:
        print('\033[31m',end='')
    print(f'{l} ', end='')

if contador == 2:
    print(f'\n\033[mO número {num} foi dividido \033[34m{contador}\033[m vezes.')
    print('ELE É PRIMO.')
else:
    print(f'\n\033[mO número {num} foi dividido \033[34m{contador}\033[m vezes.')
    print('NÃO É PRIMO.')