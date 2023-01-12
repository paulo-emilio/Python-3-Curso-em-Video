pessoas = {'nome': 'Paulo', 'sexo': 'M', 'idade': 22}
for k in pessoas.items():
    print(k)
print('=-'*30)
for k in pessoas.values():
    print(k)
print('=-'*30)
for k in pessoas.keys():
    print(k)
print('=-'*30)
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
pessoas['nome'] = 'Flávia'
pessoas['peso'] = 39.9
print(pessoas)
print('=-'*30)
print()

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Minas Gerais', "sigla": 'MG'}
brasil.append(estado1)
brasil.append(estado2)
print(f'Lista Brasil: {brasil}')
print(f'MG: {brasil[1]["sigla"]}')

