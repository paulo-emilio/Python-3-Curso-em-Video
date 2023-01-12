nome = str(input('Digite seu nome completo: '))

print('Seu nome em letras maiúsculas: ', nome.upper())
print('Seu nome em letras minúsculas: ', nome.lower())

nomejunto = nome.replace(' ', '')
print('Seu nome possui {} letras'.format(len(nomejunto)))
nomesplit = nome.split()
print('O seu primeiro nome tem {} letras'.format(len(nomesplit[0])))

