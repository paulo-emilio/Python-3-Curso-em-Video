print('\033[4m''Conversão''\033[m')
num = int(input('Número: '))
cores = {'cor1': '\033[32m',
         'cor2': '\033[36m',
         'cor3': '\033[31m',
         'fecha': '\033[m'}

base = int(input(f'''
[ {cores['cor1']}1{cores['fecha']} ] Base {cores['cor1']}Binária{cores['fecha']}
[ {cores['cor2']}2{cores['fecha']} ] Base {cores['cor2']}Octal{cores['fecha']}
[ {cores['cor3']}3{cores['fecha']} ] Base {cores['cor3']}Hexadecimal{cores['fecha']} 
Sua opção: '''))

if base == 1:
    print(f'{num} convertido para base Binária é:  {bin(num)[2:]}')

elif base == 2:
    print(f'{num} convertido para base Octal é:  {oct(num)[2:]}')

elif base == 3:
    print(f'{num} convertido para base Hexadecimal é:  {hex(num)[2:]}')

else:
    print('''PQP!
1, 2 ou 3 !!!
É simples''')
