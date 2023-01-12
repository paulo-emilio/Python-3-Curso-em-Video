from time import sleep
lista = []


def contagem(a, b, p):
    print(f'Contagem de {a} até {b} de {p} em {p}:')
    if p == 0:
        print(a, end=' ')
        print('Fim')
        exit()
    if a < b:
        cont = a
        while cont <= b:
            sleep(0.05)
            print(cont, end=' ')
            cont += p
        print()
    elif a > b:
        cont = a
        while cont >= b:
            sleep(0.05)
            print(cont, end=' ')
            cont -= p
        print()

    print('Fim!')
    print('--'*35)


# Programa Principal
contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora sua vez')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo < 0:
    passo *= -1

contagem(inicio, fim, passo)
