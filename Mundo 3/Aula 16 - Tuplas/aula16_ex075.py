numeros = (int(input('Digite o primeiro número: ')),
           int(input('Digite outro número: ')),
           int(input('Mais um: ')),
           int(input('Último: ')))
print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('Não tem 3.')
cont = 0
for n in numeros:
    if n % 2 == 0 and n != 0:
        if cont == 0:
            print('Os valores pares digitados foram: ')
        print(n, end=' - ')
        cont += 1
