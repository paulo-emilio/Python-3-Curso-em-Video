from exercicios_aula22 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moedas(p)} é {moeda.moedas(moeda.metade(p))}')
print(f'O dobro de {moeda.moedas(p)} é {moeda.moedas(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moedas(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moedas(moeda.diminuir(p, 13))}')
