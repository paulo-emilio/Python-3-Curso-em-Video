import random

n = random.randint(0, 5)
n2 = int(input('Tente adivinhar o número gerado: '))
print('Acertou!' if n == n2 else 'Errou :(')
print('Número gerado: {}'.format(n))
