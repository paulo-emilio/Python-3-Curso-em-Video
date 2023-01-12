dicionario = {}  # dicionario = dictc()
dados = {'nome': 'Paulo', 'idade': 22}
print(dados['nome'], dados['idade'])
dados['sexo'] = 'M'  # add um novo valor já com índice sexo
print(dados)
del dados['idade']  # deleta o elemento idade
print(dados)

filme = {'titulo': 'Star Wars',
         'ano': '1977',
         'diretor': 'George Lucas'
         }
print('Valores:', filme.values())  # Pega os valores (Star Wars, 19997 e George Lucas
print('Chaves', filme.keys())  # Pega as chaves (titulo, ano e diretor)
print('Itens',  filme.items())  # Pega os 2

for key, value in filme.items():
    print(f'O {key} é {value}')