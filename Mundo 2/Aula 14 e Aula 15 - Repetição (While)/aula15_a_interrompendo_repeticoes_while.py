cont = 1
while cont <= 10:
    print(cont, '->', end=' ')
    cont += 1
print('Acabou')

'''
Executando para sempre:
cont = 1
while True:
    print(cont, '->', end=' ')
    cont += 1
'''
# Para quando digitar '999'
'''
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print(f'Soma: {s}')
'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'Soma: {s}')
