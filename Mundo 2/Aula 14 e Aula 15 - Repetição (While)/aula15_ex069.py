mais18 = h_cont = m_menos20 = 0

while True:
    print('CADASTRE UMA PESSOA')
    print('=-'*15)

    idade = int(input('Idade: '))
    if idade >= 18:
        mais18 += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]  # [0] Pega só a primeira letra
        if sexo in 'M':
            h_cont += 1
        elif sexo in 'F' and idade < 20:
            m_menos20 += 1
    print('=-'*15)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]  # [0] Pega só a primeira letra
    if continuar in 'Ss':
        print('=-'*15)
    elif continuar in 'Nn':
        break

print(f'\nTotal de pessoas com mais de 18 anos: {mais18}.')
print(f'Ao todos temos {h_cont} homens cadastrados.')
print(f'E temos {m_menos20} mulheres com menos de 20 anos.')
