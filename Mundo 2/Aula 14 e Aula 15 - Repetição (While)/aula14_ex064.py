s = 0
c = 0
n = int(input('Some um número [999 para parar]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Some um número [999 para parar]: '))
print(f'Você digitou {c} números e a soma entre eles foi: {s}')
