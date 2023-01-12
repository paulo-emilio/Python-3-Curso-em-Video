matriz = [[], [], []]
n = 0
for c in range(0, 3):
    for v in range(0, 3):
        n = int(input(f'Valor [{c},{v}]: '))
        matriz[c].append(n)

print('=-'*11)
titulo = 'MATRIZ'
print(f'[{titulo:^19}]', end='')

for c in range(0, 3):
    print()
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')



'''
print(f'[{matriz[0][0]:^5}][{matriz[0][1]:^5}][{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}][{matriz[1][1]:^5}][{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}][{matriz[2][1]:^5}][{matriz[2][2]:^5}]')'''
