print('Essas Retas Podem Formar um Triângulo?')
print('=======================================')

r1 = int(input('Reta Um: '))
r2 = int(input('Reta Dois: '))
r3 = int(input('Reta Três: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Essas retas PODEM formar um triângulo!')
else:
    print('Essas retas NÃO PODEM formar um triângulo :(')
