num = [2, 5, 3, 1]
num [2] = 3  # alterando valores
num.append(7)  # adicionando 7 ao final
num.insert(2, 0)  # na posição 2 add 0. vai passar a partir do 3 para frente e colocar o 0
print(num)

num.sort()  # ordem
print(num)

num.pop()  # elimina o último valor
num.pop(2)  # elimina o valor no índice 2
print(num)

num.append(3)
print(num)
if 3 in num: # remover so se tiver num 3 na lista
    num.remove(3) # vai eliminar só o primeiro 3

valores = list()  # também pode ser criado assim: valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

# add pelo input

for cont in range(0, 2):
    valores.append(int(input('Adicione um valor: ')))
print(valores)

a = [2, 3, 4, 7]
b = a
b[2] = 8  # observe que não altera a lista. Pois quando escrito b = a, o Python liga as lista, não só as copia
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# como fazer entao:
b = a[:]  # criando uma cópia, não uma ligação
b[2] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')