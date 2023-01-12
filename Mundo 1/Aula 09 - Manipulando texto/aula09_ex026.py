frase = str(input('Digite uma frase: ')).strip().upper()
print('A frase tem {} letras "A"'.format(frase.count('A')))
print('A primeira letra "A" aparece na posilçao: ', frase.find('A'))
print('A última letra "A" aparece na posição: ',frase.rfind('A'))
