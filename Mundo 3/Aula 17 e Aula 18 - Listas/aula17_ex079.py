listanum = []
continuar = ''
while True:
    if continuar == 'N':
        break
    n = int(input('Digite um valor: '))
    if n in listanum:
        print('Valor duplicado! Não vou adicionar.')
    else:
        listanum.append(n)
        print('Valor adicionado com sucesso!')
    # continuar
    while True:
        continuar = input('Quer continuar [S/N]? ').strip().upper()[0]
        if continuar == 'S':
            print('=-' * 20)
            break
        elif continuar == 'N':
            break
        else:
            print('Somente S ou N')

print('=-' * 20)
listanum.sort()
print(f'Você digitou os valores: {listanum}')
