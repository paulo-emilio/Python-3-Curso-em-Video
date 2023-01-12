frase = str(input('Digite uma frase sem acentos: ')).strip().upper().replace(' ', '')
aocontrario = frase[::-1]
print(f'O inverso de {frase} é {aocontrario}')
if frase == aocontrario:
    print('Temos um Palíndromo!')
else:
    print('Não temos um Palíndromo :(')

# Guanabara
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntafrase = ''.join(palavras)
inverso = ''

for letra in range( (len(juntafrase) - 1), -1, -1):
    inverso += juntafrase[letra]
    
print(f'Você digitou {juntafrase}, o inverso é {inverso}')

if inverso == juntafrase:
    print('Palíndromo!')
else:
    print('Não Palíndromo.')
