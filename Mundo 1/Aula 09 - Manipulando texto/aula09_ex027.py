nome = str(input("Digite um nome completo: ")).strip()
print('Primeiro nome: ', nome.split()[0])
print('Último nome: ', nome.split()[-1])
print('Primeira letra do último nome:', nome.split()[-1][0])
