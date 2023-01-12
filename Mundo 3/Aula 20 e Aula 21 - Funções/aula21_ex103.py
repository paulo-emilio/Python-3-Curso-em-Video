def ficha(jogador='<desconhecido>', gols='0'):
    if jogador.isalpha():
        j = jogador
    else:
        j = '<desconhecido>'
    if gols.isnumeric():
        g = gols
    else:
        g = '0'
    print(f'O Jogador {j} fez {g} gol(s).')


ficha(jogador=input("Jogador: ").capitalize(), gols=input("Gols: "))
