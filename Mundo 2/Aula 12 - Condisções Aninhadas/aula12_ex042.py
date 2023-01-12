print('Essas Retas Podem Formar um Triângulo?')
print('=======================================')

r1 = int(input('Reta Um: '))
r2 = int(input('Reta Dois: '))
r3 = int(input('Reta Três: '))
resultado = ''

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    resultado = 'Essas retas PODEM formar um triângulo!'
    print(resultado)
else:
    resultado = 'Essas retas NÃO PODEM formar um triângulo :('
    print(resultado)

if resultado == 'Essas retas PODEM formar um triângulo!':
    if r1 == r2 == r3:
        print('Triângulo Equilátero.')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Triângulo Isósceles.')
    elif r1 != r2 != r3 != r1:
        print('Triângulo Escaleno.')
