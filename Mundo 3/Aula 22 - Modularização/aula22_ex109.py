from exercicios_aula22 import ex109

p = float(input('Digite o preço: R$ '))
print(f'A metade de {ex109.moedas(p)} é {ex109.metade(p,False)}')  # False ou True, vai formatar ou nao o preço
print(f'O dobro de {ex109.moedas(p)} é {ex109.dobro(p)}')
print(f'Aumentando 10%, temos {ex109.aumentar(p, 10,False)}')
print(f'Reduzindo 13%, temos {ex109.diminuir(p, 13)}')
