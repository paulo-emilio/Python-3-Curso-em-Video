lista = []
continuar = ''

while True:
    if continuar == 'N':
        break
    lista.append(int(input('Digite um valor: ')))
    # Continuar?
    while True:
        continuar = input('Continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Tente novamente')

print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')