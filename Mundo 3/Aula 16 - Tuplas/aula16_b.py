a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  # Junta as tuplas em sequência
print(c)
print(f'Quantas vezes tem 5 na tupla C: {c.count(5)}')
print(f'Qual posição está o 5: {c.index(5)}')
print(f'Qual posição está o 5 depois da posição 0: {c.index(5, 1)}')  # Deslocamento
print('')

pessoa = 'Gustavo', 39, 'Masculino', 99.88
print(pessoa)

del pessoa  # Deleta pessoa
