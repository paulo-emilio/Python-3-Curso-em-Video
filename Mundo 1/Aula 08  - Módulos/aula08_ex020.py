'''Tentativa que não deu certo por ser possível sortear o mesmo input mais de uma vez
import random
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1,a2,a3,a4]
listagem = random.choices(lista, k=4)
print(listagem)
'''
from random import shuffle
a1 = str(input('ALUNO 01: '))
a2 = str(input('ALUNO 02: '))
a3 = str(input('ALUNO 03: '))
a4 = str(input('ALUNO 04: '))
lista = [a1,a2,a3,a4]
shuffle(lista)
print('Ordem:', lista)