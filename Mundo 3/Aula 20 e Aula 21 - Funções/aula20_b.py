'''def soma(a, b):
    print(f'A = {a} B = {b}')
    s = a + b
    print(s)


# Programa Principal
soma(5, 4)
soma(50, 49)
soma(500, 499)
soma(b=5000, a=4999)'''


def contador(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print('Fim!')


contador(1, 2, 3)
contador(4, 5, 6)

def count (*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


count(1, 2, 3)
count(11, 22, 33)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 6, 8, 10, 12, 16, 18, 22]
dobra(valores)
print('=-'*30)
print(valores)
