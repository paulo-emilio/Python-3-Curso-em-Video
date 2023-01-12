estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('UF: ')).capitalize()
    estado['sigla'] = str(input('Sigla: ')).upper()
    brasil.append(estado.copy())
print(brasil)
print('=-'*30)
for e in brasil:
    print(e)
print('=-'*30)
for e in brasil:
    print()
    for k, v in e.items():
        print(f'{k}: {v:8}',end='')
print()
for e in brasil:
    print()
    for k, v in e.items():
        print(v, end=' ')