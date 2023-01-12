'''
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo Valor:'))
n3 = float(input('Terceiro Valor: '))

lista = [n1, n2, n3]

print('\nO maior valor é: ', max(lista))
print('O menor valor é: ', min(lista), '\n\n')
'''
#Viagem do Guanabara

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

sobra = a
if maior == a and menor == c:
    sobra = b
if maior == c and menor == a:
        sobra = b
if maior == a and menor == b:
    sobra = c
if maior == b and menor == a:
    sobra = c


cores = {'vermelho': '\033[4;31m',
         'ciano': '\033[1;36m',
         'preto_branco': '\033[7;30m',
         'limpa': '\033[m'}

print('O maior valor digitado foi: {}{}{}'.format(cores['ciano'], maior, cores['limpa']))
print('O menor valor digitado foi: {}{}{}'.format(cores['vermelho'], menor, cores['limpa']))
print(f"O valor do meio foi: {cores['preto_branco']}{sobra}{cores['limpa']}")
