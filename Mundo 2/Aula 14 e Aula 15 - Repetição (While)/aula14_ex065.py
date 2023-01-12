continuar = 'S'
n = c = s = m = ma = me = 0

while continuar in 'Ss':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if c == 1:
        ma = me = n
    if n > ma:
        ma = n
    if n < me:
        me = n
    continuar = str(input('Quer continuar? [S/N]? ')).strip().upper()
m = s/c

print(f'\nVocê digitou {c} números e a média foi {m:.2f}')
print(f'O maior valor foi {ma} e o menor foi {me}')