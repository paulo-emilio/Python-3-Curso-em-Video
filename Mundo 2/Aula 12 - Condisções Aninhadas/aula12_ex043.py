peso = float(input('Digite deu peso em KG: '))
altura = float(input('Digite sua altura em metros: '))
#IMC = Peso / Altura²
imc = peso / (altura ** 2)
print('')

print(f'Seu IMC é: {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do peso. :(')

elif 18.5 <= imc < 25:
    print('Peso ideal! :D')

elif 25 <= imc < 30:
    print('Sobrepeso!!')

elif 30 <= imc <= 40:
    print('Obesidade! :o')

else:
    print('Obesidade Mórbida!!!!!!!!!! :0')
