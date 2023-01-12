print('  Controle de Terrenos')
print('-' * 20)


def terreno(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a} m²')


# Programa Principal
terreno(l=float(input('Largura (m): ')), c=float(input('Comprimento (m): ')))
