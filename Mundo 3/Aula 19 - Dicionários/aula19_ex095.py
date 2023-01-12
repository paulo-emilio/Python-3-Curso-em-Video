todosjogadores = []
jogador = {}
gols = []
id = 0
while True:
    id += 1
    jogador['ID'] = id
    jogador['Nome'] = input('Nome do jogador: ').strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['Gols'] = gols.copy()
    jogador['Total'] = sum(gols)
    gols.clear()
    todosjogadores.append(jogador.copy())
    jogador.clear()
    while True:
        rsp = input('Continuar? [S/N]: ').strip().upper()[0]
        if rsp in 'SN':
            break
        else:
            print('Erro! Somente S ou N')
    if rsp == 'N':
        break
print('=-'*20)
print('ID   Nome      Gols       Total')
print('--'*20)
for j in range(0, len(todosjogadores)):
    for k, v in todosjogadores[j].items():
        if k == 'ID':
            print(f'{v:<5}', end='')
        if k == 'Nome':
            print(f'{v:<10}', end='')
        if k == 'Gols':
            print(f'{v}', end='')
        if k == 'Total':
            print(f'    {v:>}', end='')
    print()
print('=-'*30)
while True:
    while True:
        mais = int(input('Mostrar dados de qual jogador? ([0] para parar): '))
        print('=-' * 30)
        if 0 <= mais <= len(todosjogadores):
            break
        else:
            print('Tente novamente')
    if mais == 0:
        break
    for j in todosjogadores:
        for k, v in j.items():
            if k == 'ID' and v == mais:
                print(f'Levantamento do jogador {j["Nome"]}:')
                for c, g in enumerate(j['Gols']):
                    print(f'No jogo {c+1} fez {g} gols ')


