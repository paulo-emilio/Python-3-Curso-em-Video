# Parâmetros opcionais


def somar(a=0, b=0, c=0):
    s = a+b+c
    print(f'A soma vale {s}')


somar(5, 5, 5)
somar(5, 5)  # não passando 'c', 'c' vai valer 0
somar()  # todos vao valer 0
somar(c=5, a=5)
