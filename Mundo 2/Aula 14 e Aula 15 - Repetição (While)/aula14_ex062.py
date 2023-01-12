print('''Gerador de PA
===================''')
p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
t = int(input('Termos: '))
print('')
m = 1
c = 0

while m != 0:
    while t != 0:
        print(f'{p} ->', end=' ')
        p += r
        t -= 1
        c += 1
    print('PAUSA\n')
    m = int(input('Quantos termos você quer mostrar mais? '))
    print('')
    t += m
print(f'Prograssão finalizada com {c} termos mostrados.')