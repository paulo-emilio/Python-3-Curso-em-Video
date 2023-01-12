from time import sleep
operacao = 4

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

while operacao != 5:
    operacao = int(input(f'''
Números: {n1} e {n2}
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair
Operação: '''))
    if operacao == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif operacao == 2:
            print(f'{n1} x {n2} = {n1*n2}')
    elif operacao == 3:
        if n1 > n2:
                print(f'O maior número é: {n1}')
        elif n2 > n1:
                print(f'O maior número é: {n2}')
    elif operacao == 4:
        print('Informe os números novamente:')
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    elif operacao == 5:
        print('Finalizando...')
        sleep(1)
        exit()
    else:
        print('Opção inválida!')
    sleep(2)
