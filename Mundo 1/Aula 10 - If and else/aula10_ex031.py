km = float(input('Distância da Viagem: '))
if km <= 200:
    valor = km * 0.5
else:
    valor = km * 0.45
print('Valor da viagem: R${:.2f}'.format(valor))