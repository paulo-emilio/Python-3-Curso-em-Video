jogador = {'Nome': input('Nome do Jogador: ').strip().capitalize()}
golsporpartida = []
numpartidas = int(input('Quantas partidas ele jogou? '))
for c in range(0, numpartidas):
    golsporpartida.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['Gols'] = golsporpartida
jogador['Total'] = sum(golsporpartida)

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'{k}: {v}')
print('-='*30)

print(f'O Jogador {jogador["Nome"]} jogou {numpartidas} partidas')
for c, g in enumerate(jogador['Gols']):
    print(f'  -> Na partida {c+1}, fez {g} gols')
print('  ---------------------------')
print(f'               Total: {jogador["Total"]:2} gols')