print('''
==========================
    TERMOS DE UMA PA
==========================''')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = int(input('Quantos termos: '))
count = 0

print('\nPA:', end=' ')

while count < termos:
    print(f'{primeiro}', end='')
    print(' -> ' if count < termos - 1 else '', end='')
    primeiro += razao
    count += 1
