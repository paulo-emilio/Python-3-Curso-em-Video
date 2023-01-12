#método básico:
'''
print('Calcule a hipotenusa de um triângulo retângulo:')

catoposto = float(input('Cateto Oposto: '))
catadjacente = float(input('Cateto adjacente: '))

hipotenusa = (catoposto ** 2 + catadjacente ** 2) ** (1/2)

print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))
'''
#importando math e usando o hypot:
import math

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))

hi = math.hypot(co,ca)
print('A hipotenusa mede: {:.2f}'.format(hi))

#Importar direto somente o que vou usar:
from math import hypot
hi = hypot(co,ca)
print('A hipotenusa mede: {:.2f}'.format(hi))

