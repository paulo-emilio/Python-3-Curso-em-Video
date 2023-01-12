'''
num = str(input('Digite um número de 0 a 9999: '))
print('Unidade: ',num[-1])
print('Dezena: ', num[-2])
print('Centena ', num[-3])
print('Milhar: ', num[-4])
''' #dando erro pq se digitar um número com menos de 4 digitos nao lê todos prints
import math

num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: ', u)
print('Dezena: ',d)
print('Centena: ', c)
print('Milhar: ', m)

