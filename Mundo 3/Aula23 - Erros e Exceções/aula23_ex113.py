def leiaInt(x):
    while True:
        try:
            n = int(input(x).replace(' ', ''))
        except KeyboardInterrupt:
            print('\n\033[036mEntrada de dados interrompida pelo usuário. (0) Adicionado.\033[m')
            return 0
        except (ValueError, TypeError):
            print(f'\033[031mDigite um número INTEIRO!\033[m\n')
        else:
            return n


def leiaFloat(fl):
    while True:

        try:
            n = float(input(fl).replace(' ', '').replace(',', '.'))
        except KeyboardInterrupt:
            print('\n\033[036mEntrada de dados interrompida pelo usuário. (0) Adicionado\033[m')
            return 0
        except (ValueError, TypeError):
            print(f'\033[031mDigite um número RACIONAL!\033[m\n')
        else:
            return n


i = leiaInt('Número inteiro: ')
f = leiaFloat('\nNúmero racional: ')

print(f'\nO número inteiro digitado foi: {i}. O número racional digitado foi: {f}')
