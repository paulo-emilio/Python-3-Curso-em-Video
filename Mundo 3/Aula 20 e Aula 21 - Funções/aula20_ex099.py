from time import sleep


def analise(nums):
    print('Analisando valores passados...')
    maior = nums[0]
    cont = 0
    for c in nums:
        sleep(0.2)
        print(c, end=' ')
        if c > maior:
            maior = c
        cont += 1
    print(f'// Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}.')


lista = []
rsp = ' '
while rsp not in 'N':
    n = int(input('Valor: '))
    rsp = input('Continuar? ').strip().upper()[0]
    lista.append(n)
analise(lista)
