from datetime import date
print('\033[4:36m''Confederação Nacional de Natação''\033[m')
print('')
ano_nascimento = int(input('Ano de Nascimento do Atleta: '))
idade = date.today().year - ano_nascimento
print(f'Idade: {idade}')

if idade < 0:
    print('O atleta precisa ter nascido para participar.')

elif 0 <= idade <= 9:
    print('Categoria: MIRIM')

elif idade <= 14:
    print('Categoria: INFANTIL')

elif idade <= 19:
    print('Categoria: JUNIOR')

elif idade <= 25:
    print('Categoria: SÊNIOR')

elif idade > 25:
    print('Categoria: MASTER')
