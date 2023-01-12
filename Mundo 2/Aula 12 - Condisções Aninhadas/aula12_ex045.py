from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

jogador = int(input('''Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual é sua jogada? '''))

reclamacoes = ('Não consegue né Moisés...', 'Joga direito mula.', '0, 1 ou 2, É tão complexo assim?')
if jogador > 2:
    print(reclamacoes[computador])
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO !!!')

    print('-=' * 14)

    print(f'Computador jogou: {itens[computador]}')
    print(f'Você jogou: {itens[jogador]}')
    print('-=' * 14)

    if computador == 0:  # Pedra
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('VOCÊ VENCEU!')
        elif jogador == 2:
            print('COMPUTADOR GANHOU')

    elif computador == 1:  # Papel
        if jogador == 0:
            print('COMPUTADOR GANHOU.')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('VOCÊ VENCEU!')

    elif computador == 2:  # Tesoura
        if jogador == 0:
            print('VOCÊ VENCEU!')
        elif jogador == 1:
            print('COMPUTADOR GANHOU')
        elif jogador == 2:
            print('EMPATE')
