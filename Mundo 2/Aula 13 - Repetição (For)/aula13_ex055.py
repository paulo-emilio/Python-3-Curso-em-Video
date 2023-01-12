maiorpeso = 0
menorpeso = 9999

for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso

print(f'''O MAIOR peso foi de {maiorpeso} Kg
O MENOR peso foi de {menorpeso} Kg''')


#Guanabara
maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'''O MAIOR peso foi de {maior} Kg
O MENOR peso foi de {menor} Kg''')


# Thais Melo
'''
lst=[]  #lista vazia
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    lst += [peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lst))  #maximo valor da lista
print('O Menor peso foi:', min(lst))  #minimo valor da lista
'''