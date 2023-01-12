soma = cont = 0
n = int(input('Digite um valor [0 - Parar]: '))
while True:
    soma += n
    cont += 1
    n = int(input('Digite um valor [0 - Parar]: '))
    if n == 0:
        break

print(f'\nA soma dos {cont} valores foi {soma}!')