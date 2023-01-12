lista = [[], [], []]
somapar = somaterceira = maiorsegunda = 0
for c in range(0, 3):
    for v in range(0, 3):
        n = int(input('Digite um número: '))
        lista[c].append(n)
        if n % 2 == 0:  # Soma pares
            somapar += n
        if v == 2:  # Soma da terceira COLUNA
            somaterceira += n
        if c == 1 and v == 0:  # Maior valor da segunda linha
            maiorsegunda = n
        if c == 1 and n > maiorsegunda:
            maiorsegunda = n
# Print MATRIZ
print('=-'*20)
for val in range(0, 3):
    for l in range(0, 3):
        print(f'[{lista[val][l]:^3}]', end='')
    print()

print('=-'*20)
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somaterceira}.')
print(f'O maior valor da segunda linha é {maiorsegunda}.')
