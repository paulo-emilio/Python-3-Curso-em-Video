nome = str(input('Qual o seu nome? ')).strip().upper()
if nome == 'LOKI':
    print('Que nome lindo!')
else:
    print('Seu nome é normal.')
print('BOM DIA, {}!'.format(nome))

print('Notas:')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) / 2
print('A sua média foi: {:.1f}'.format(m))
print('Você Passou!' if m >= 6.0 else 'Estude mais')
