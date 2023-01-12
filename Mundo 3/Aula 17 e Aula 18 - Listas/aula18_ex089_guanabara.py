lista = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2) / 2
    lista.append([nome, [n1, n2], media])
    # continuar?
    rsp = input('Continuar? ')
    if rsp in 'Nn':
        break

for i, a in enumerate(lista):
    print(f'{i:<2} - {a[0]:^10} - {a[2]:>.1f}')

while True:
    opc = int(input('Notas [ID]: '))
    if opc == 999:
        break
    elif 0 <= opc <= len(lista)-1:
        print(f'Notas de {lista[opc][0]}: {lista[opc][1]}')
    else:
        print('try again bro')
