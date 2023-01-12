numeros = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez'
continuar = ''
while True:
    if continuar == 'N':
        break
    n = int(input('Digite um número de 0 a 10: '))
    if 0 <= n <= 10:
        print(f'Você digitou o número: {numeros[n]}\n')
        while continuar != 'N' or 'S':
            continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
            if continuar == 'S':
                    print('')
                    break
            elif continuar == 'N':
                break
            else:
                print('Tente novamente.')
    else:
        print('Tente novamente.')



print('Fim')