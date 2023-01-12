# Importando os moeda e dado de pacotes
# (usar o ponto para definir quias 'pastas' dentro de cada 'pasta'

from exercicios_aula22.ex111.utilidadescev import moeda, dado

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 20, 12)
