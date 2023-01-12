def linha(tam=42):
    return '-' * tam


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


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[34m{c}\033[m - \033[36m{item}\033[m')
        c += 1
    print(linha())
    opcao = leiaInt('Sua opção: ')
    print(linha())
    return opcao