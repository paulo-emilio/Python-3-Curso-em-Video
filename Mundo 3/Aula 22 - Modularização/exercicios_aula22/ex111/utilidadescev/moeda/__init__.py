def metade(n, f=True):
    if f:
        return moedas(n/2)
    elif not f:
        return n/2


def dobro(n, f=True):
    if f:
        return moedas(n*2)
    else:
        return n*2


def aumentar(n, a, f=True):
    if f:
        return moedas(n * ((a/100)+1))
    else:
        return n * ((a/100)+1)


def diminuir(n, d, f=True):
    porc = n * (d/100)
    if f:
        return moedas(n - porc)
    else:
        return n - porc


def moedas(n=0, m='R$'):
    return f'{m} {n:.2f}'.replace('.', ',')


def resumo(n=0, a=0, r=0):
    print('-------------------------------'
          '\n        RESUMO DO VALOR'
          '\n-------------------------------')
    print(f'Preço analisado: \t{moedas(n)}')
    print(f'Dobro do preço:  \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'{a}% de aumento: \t{aumentar(n,a)}')
    print(f'{r}% de redução: \t{diminuir(n,r)}')
