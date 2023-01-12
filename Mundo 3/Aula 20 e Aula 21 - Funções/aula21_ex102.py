def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar o não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('=-'*30)
    r = 1
    for c in range(n, 0, -1):
        r *= c
        if show is True:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} = {r}')
        else:
            if c == 1:
                print(r)


# Programa Principal
fatorial(int(input('Número para fatorar: ')), True)
print()
help(fatorial)
