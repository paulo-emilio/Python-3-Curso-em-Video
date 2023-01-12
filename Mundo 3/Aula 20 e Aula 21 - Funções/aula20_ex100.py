from random import randint
from time import sleep


def aleatorio(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    cont = 0
    while cont < 5:
        n = randint(1, 10)
        if n not in lista:
            lista.append(n)
            print(n, end=' ')
            cont += 1
        sleep(0.3)
    print('Pronto!')


def somando(listasoma):
    soma = 0
    for n in listasoma:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {listasoma}, temos... ', end='')
    sleep(2)
    print(soma)


nums = []
aleatorio(nums)
sleep(1)
somando(nums)
