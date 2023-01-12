# listas dentro de listas
pessoas = [['Pedro', 25],['Maria', 19], ['João', 32]]
print(pessoas[0][0])  # Pedro
print(pessoas[2][1])  # 32
print(pessoas[1])  # [Maria, 19]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')


print('=-'*20)
# testes guana
teste = []
teste.append('Paulo')
teste.append(22)
galera = []
galera.append(teste[:])
teste[0] = 'Flávia'
teste[1] = 23
galera.append(teste[:])
print(galera)

print('=-'*20)
gal = []
dado = []
maior = menor = 0
for c in range(0, 3):
    dado.append(input('Nome: ').capitalize())
    dado.append(int(input('Idade: ')))
    gal.append(dado[:])
    dado.clear()

print(gal)

for p in gal:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} maiores de idade e {menor} menores de idade')

'''
if 30 not in gal:
    exemplo
'''