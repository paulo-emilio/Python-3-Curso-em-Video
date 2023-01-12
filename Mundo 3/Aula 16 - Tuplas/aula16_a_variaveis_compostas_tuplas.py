lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(sorted(lanche))  # Ordem alfabética
print(lanche[1])  #Suco
print(lanche[0:3])  # Hambúrguer até Pizza (Não considera o '3')
print(lanche[2:])  # 2 até o final
print(lanche[:2])  # Início até o 1
print(lanche[-2:])  # Começa na Pizza até o final
print('')
# Tuplas são imutáveis
# lanche[1] = 'Refrigerante'  - Dá erro

# Imprimir bonito:
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print(len(lanche))  # Quantos elementos tem na tupla

# Outra forma usar o for:
for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]}')
    print(f'Vou comer {lanche[cont]} que está na posição {cont}')  # Mostrando a posição
print('')
# Outra forma mostrar o dado e a posição
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} que está na posição: {pos}')

