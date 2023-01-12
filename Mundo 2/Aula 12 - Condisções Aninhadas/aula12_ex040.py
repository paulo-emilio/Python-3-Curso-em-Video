nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print(f'Média: {media}')

if media < 5.0:
    print('Reprovado.')

elif 6.9 >= media >= 5.0:
    print('Recuperação.')

else:
    print('Aprovado.')
