nomes = []
nota1 = []
nota2 = []
media = []
while True:
    nomes.append(input('Nome: ').capitalize())
    n1 = float(input('Nota 1: '))
    nota1.append(n1)
    n2 = float(input('Nota 2: '))
    nota2.append(n2)
    media.append((n1+n2)/2)
    # continuar
    continuar = input('Continuar? ').strip().upper()[0]
    if continuar in 'N':
        break
print('ID -    NOME    - MÉDIA')
for id, nome in enumerate(nomes):
    print(f'{id}  - {nome:^10}', end=' - ')
    print(f'{media[id]:.1f}')

while True:
    mt = int(input('Mostrar notas [ID]: '))
    if mt == 999:
        break
    elif 0 <= mt < len(nomes):
        print(f'Notas de {nomes[mt]} -> Nota 1: [{nota1[mt]}] Nota 2: [{nota2[mt]}]')
    else:
        print('Tente novamente')

