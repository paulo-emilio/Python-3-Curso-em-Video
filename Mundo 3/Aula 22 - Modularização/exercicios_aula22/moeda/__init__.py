def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def aumentar(n, a):
    return n * (a/100+1)


def diminuir(n, d):
    porc = n * (d/100)
    return n - porc


def moedas(n=0, m='R$'):
    return f'{m} {n:.2f}'.replace('.', ',')
