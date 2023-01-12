def somar(a=0, b=0, c=0):
    s = a+b+c
    return s  # vai retornar o valor para onde a função foi chamada


r1 = somar(3, 2, 5)  # 'r1' recebe 's' que é 3+2+5
r2 = somar(4, 4)  # 'r2' recebe 's' que é 4+4
print(f'r1 = {r1}''\n'
      f'r2 = {r2}')
print(f'somar(6) = {somar(6)}')  # printa 's'
