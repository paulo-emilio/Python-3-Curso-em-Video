'''pmenor = []
pmaior = []
cont = maior = menor = 0
while True:
    nome = input('Nome: ').capitalize()
    peso = float(input('Peso: '))
    if cont == 0:
        maior = menor = peso
    if peso == maior:
        pmaior.append(nome)
    elif peso > maior:
        maior = peso
        pmaior.clear()
        pmaior.append(nome)

    if peso == menor:
        pmenor.append(nome)
    elif peso < menor:
        menor = peso
        pmenor.clear()
        pmenor.append(nome)

    cont += 1
    continuar = input('Continuar? (S/N) ').strip().upper()[0]
    if continuar in 'N':
        break

print('=-'*25)
print(f'Ao todo você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior}KG, de {pmaior}')
print(f'O menor peso foi de {menor}KG, de {pmenor}')
'''

# Guanabara
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    print(princ)
    temp.clear()

    continuar = input('Continuar? (S/N) ').strip().upper()[0]
    if continuar in 'N':
        break

print('=-'*25)
print(f'Os dados foram {princ}')
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg de: ',end='')
for peso in princ:
    if peso[1] == mai:
        print(f'[{peso[0]}]', end=' ')
print(f'\nO menor peso foi de {men}Kg de: ', end='')
for peso in princ:
    if peso[1] == men:
        print(f'[{peso[0]}]', end=' ')