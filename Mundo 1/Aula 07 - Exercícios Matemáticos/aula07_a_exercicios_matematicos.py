n1 = int (input('Digite um valor: '))
n2 = int (input('Digite um valor: '))
s= n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rd = n1 % n2 #resto da divisão
print('A soma é {}, A multiplicação é {}. \nA potência é {},'.format(s,m,e), end=' ')
print('a divisão é {}, e a divisão inteira é {}'.format(d,di))