from datetime import date
maiorcont = 0
menorcont = 0

for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = date.today().year - nascimento

    if idade >= 18:
        maiorcont += 1
    elif idade < 18:
        menorcont += 1

print(' ')

print(f'''{maiorcont} Maiores de Idade
{menorcont} Menores de Idade''')
