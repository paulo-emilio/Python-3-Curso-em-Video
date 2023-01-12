import math

n1 = int(input('Digite um número: '))
raiz = math.sqrt(n1)

print('A raiz de {} é igual a: {}'.format(n1,raiz))
print('A raiz de {} arredondada para cima é igual a: {}'.format(n1,math.ceil(raiz)))
print('A raiz de {} arredondada para baixo é igual a: {}'.format(n1,math.floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(n1, raiz))

# Outra forma de importar
from math import sqrt, floor

n1 = int(input('Digite um número:' ))
raiz = sqrt(n1)

print('A raiz de {} é igual a: {}'.format(n1,floor(raiz)))

# Ver quais bibliotecas posso importar por padrão: www.python.org > Docs > Escolher versão > Referência da Biblioteca
