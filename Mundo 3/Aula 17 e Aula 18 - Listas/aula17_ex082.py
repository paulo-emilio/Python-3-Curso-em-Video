lista = []
pares = []
impares = []
'''while True:
    n = int(input('Valor: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    continuar = input('Continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break '''
# Guanabara
while True:
    lista.append(int(input('Valor: ')))
    resp = input('Continuar? S/N ').strip()[0]
    if resp in 'Nn':
        break

for c, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímapares é: {impares}')