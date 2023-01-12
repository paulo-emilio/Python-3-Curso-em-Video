numeros = []
maior = menor = pmaior = pmenor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Adicione um número para a posição {c}: ')))
    if c == 0:
        maior = menor = numeros[c]
    if numeros[c] > maior:
        maior = numeros[c]
        pmaior = c
    if numeros[c] < menor:
        menor = numeros[c]
        pmenor = c

'''print(f'\nO maior valor foi {maior} na posição {pmaior}.')
print(f'O menor valor foi {menor} na posição {pmenor}.')'''

# Ou
print(f'O maior valor foi {maior}  nas posições: ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}. ', end='')
print(f'\nO menor valor foi {menor} na(s) posicõe(s) ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}. ', end='')