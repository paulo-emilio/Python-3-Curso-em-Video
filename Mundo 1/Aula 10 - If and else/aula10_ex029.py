vel = int(input('Velocidade do carro: '))
if vel > 80:
    print('MULTADO!')
    v_acima = vel - 80
    print('Você estava a {} km/h acima do limite da via (80km/h).'.format(v_acima))
    print('Você deverá pagar R${} de multa.'.format(v_acima*7.00))
else:
    print('Tudo certo! Você estava dentro do limite.')

