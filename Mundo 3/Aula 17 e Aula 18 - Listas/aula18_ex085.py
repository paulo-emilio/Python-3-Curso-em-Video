numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        if n == 0:
            print('Zero é nulo')
        else:
            numeros[0].append(n)
    elif n % 2 == 1:
        numeros[1].append(n)


numeros[0].sort()
numeros[1].sort()
print(f'Pares: {numeros[0]}')
print(f'Ímpares: {numeros[1]}')