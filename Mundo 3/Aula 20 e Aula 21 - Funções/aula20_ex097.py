def escreva(msg):
    tam = len(msg) + 2
    print('~'*tam)
    print(f' {msg}')
    print('~'*tam)


# Programa Principal
escreva(input('Título: '))
