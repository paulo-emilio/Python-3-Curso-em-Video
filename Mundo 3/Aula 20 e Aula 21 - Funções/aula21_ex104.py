def leiaInt():
    """
    -> ler um número e retorná-lo
    :return: n
    """
    while True:
        n = input('Digite um número: ').strip()
        if n.isnumeric():
            return n
        else:
            print('\033[31mERRO: < SOMENTE NÚMEROS >\033[m')


num = leiaInt()
print(f'Número salvo em num: {num}')