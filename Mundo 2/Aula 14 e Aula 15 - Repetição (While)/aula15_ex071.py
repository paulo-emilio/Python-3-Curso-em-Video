print('='*30)
print('{:^30}'.format('BANCO PPG'))
print('='*30)

c50 = c20 = c10 = c1 = sub = 0

valor = int(input('Qual valor você quer sacar? '))

while True:
    if valor >= 50:
        c50 += 1
    elif valor < 50:
        break
    valor -= 50
while True:
    if valor >= 20:
        c20 += 1
    elif valor < 20:
        break
    valor -= 20
while True:
    if valor >= 10:
        c10 += 1
    elif valor < 10:
        break
    valor -= 10
while True:
    if valor >= 1:
        c1 += 1
    elif valor < 1:
        break
    valor -= 1
print('=-'*15)
if c50 > 0:
    print(f'Total de {c50} cédulas de R$ 50')
if c20 > 0:
    print(f'Total de {c20} cédulas de R$ 20')
if c10 > 0:
    print(f'Total de {c10} cédulas de R$ 10')
if c1 > 0:
    print(f'Total de {c1} cédulas de R$ 1')
print('=-'*15)
print('Volte sempre ao BANCO PPG! Tenha um bom dia!')

# Guanabara
print('='*30)
print('{:^30}'.format('BANCO DO GUANA'))
valor = int(input('Sacar: '))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        totced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
print('Falou!')