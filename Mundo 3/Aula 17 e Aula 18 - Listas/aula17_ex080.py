lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final')
    elif n < lista[0]:
        lista.insert(0, n)
        print('Adicionado ao início')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('=-'*12)
print(lista)

'''lista = []
cont = 0
while cont < 5:
    n = int(input('Valor: '))
    if cont == 0 or n > lista[-1]:
        lista.append(n)
    elif n < lista[0]:
        lista.insert(0, n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
    cont += 1
print(lista)'''














