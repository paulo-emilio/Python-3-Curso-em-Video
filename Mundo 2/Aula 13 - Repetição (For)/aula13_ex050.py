soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Valor para soma: '))
    if n % 2 == 0:
        soma += n
        cont = cont + 1
print(f'Soma dos {cont} valores pares foi: {soma}')
