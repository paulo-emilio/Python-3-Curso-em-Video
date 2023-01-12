'''import math

print('Calcule o Seno, Cosseno e Tangente de um ângulo:')

angulo = float(input('Ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('Seno: {:.2f}'.format(sen))
print('Cosseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tan))'''

from math import sin, cos, tan, radians

an = float(input('Digite o ângulo: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(sen,cos, tan))
