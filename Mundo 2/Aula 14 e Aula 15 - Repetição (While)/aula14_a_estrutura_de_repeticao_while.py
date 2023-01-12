'''for c in range(1, 10):
    print(c,end= '')
print('Fim')'''
# Sabendo o fim:
c = 1
while c < 10:
    print(c,end= '-')
    c += 1
print('Fim!')

# Quando nao se sabe o fim:
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

# Doideira
n = 100
par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n% 2 == 0:
            par += 1
            impar += 1


print(f'Você digitou {par} números pares e {impar} números ímpares.')