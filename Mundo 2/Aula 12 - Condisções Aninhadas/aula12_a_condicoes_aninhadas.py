nome = str(input('Qual é seu nome? '))
if nome == 'Paulo':
    print('Que nome Bonito!')
elif nome == 'José' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Carla Flávia Rafaela Ana':
    print('Belo nome feminino!')

print(f'Tenha um bom dia {nome}')
