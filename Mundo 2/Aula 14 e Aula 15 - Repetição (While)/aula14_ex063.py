print('''Sequência de Fibonacci
-------------------------''')
termos = int(input('Quantos termos você quer mostrar? ')) - 2
n = 0
s = 1
t = 0

print(f'{n} -> {s} ->', end=' ')

while termos > 0:
    t = n + s
    print(f'{t} ->', end=' ')
    n = s
    s = t
    termos -= 1
print('FIM')
