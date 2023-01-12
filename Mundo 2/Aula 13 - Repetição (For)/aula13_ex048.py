soma = 0
cont = 0
for c in range(1, 501, 2):  # 2 é pra pegar so ímpares
    if c % 3 == 0:
        cont = cont + 1
        soma += c  # soma = soma + c
print(f'Foram somados {cont} valores.')
print(f'A soma de todos os valores solicitados é {soma}')


