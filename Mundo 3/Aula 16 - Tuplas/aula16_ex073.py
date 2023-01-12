serie_a = 'Cruzeiro', 'Palmeiras', 'Flamengo', 'Fluminense', 'Atlético PR', 'São Paulo', 'Goiás', 'Grêmio', 'Vasco', \
          'Botafogo', 'Bahia', 'Bragantino', 'Internacional', 'América MG', 'Santos', 'Fortaleza', 'Galo', 'Curitiba', \
          'Avaí', 'Chapecoense'
print(serie_a)
print('=-' * 40)
print(f'G4: {serie_a[0:4]}')
print('=-' * 40)
print(f'Z4: {serie_a[-4:]}')
print('=-' * 40)
print(f'Ordem Alfabética: {sorted(serie_a)}')
print('=-' * 40)
print(f'Chapecoense está na {serie_a.index("Chapecoense") + 1}ª colocação')

