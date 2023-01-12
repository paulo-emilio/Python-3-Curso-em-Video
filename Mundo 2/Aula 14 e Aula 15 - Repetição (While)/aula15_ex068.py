from random import randint
from time import sleep

c = 0
t = str

print('=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*10)

while True:
    n = int(input('Diga um valor: '))
    opcao = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()
    pc = randint(1, 2)
    soma = n + pc
    sleep(1)

    if opcao == 'P':
        t = 'Par'
    elif opcao == 'I':
        t = 'Ímpar'

    print(f'Você jogou {n}. O PC jogou: {pc}. Resultado: {n + pc}. Você pediu {t}.')
    print('*' * 60)

    if soma % 2 == 0 and opcao in 'pP' or soma % 2 != 0 and opcao in 'Ii':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        c += 1
    elif soma % 2 == 0 and opcao in 'Ii' or soma % 2 != 0 and opcao in 'Pp':
        print(f'GAME OVER! Você venceu {c} vezes.')
        break
    else:
        print('Digita direito.')
