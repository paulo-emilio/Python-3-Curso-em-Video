print('''
==========================
    10 TERMOS DE UMA PA
==========================''')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + 10 * razao

for c in range(primeiro, decimo, razao):
    print(c, end=' -> ')

print('Done! ')
