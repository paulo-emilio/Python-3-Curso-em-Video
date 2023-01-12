lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche[3] = 'Picolé'  # Tira o pudim, põe Picolé
lanche.append('Cookie')  # Criar novo elemento no final da lista
lanche.insert(0, 'Cachorro quente')  # Abre o espaço no local desejado e adiciona o novo elemento, reformulando a contagem
# Eliminando elementos (também reposiciona a contagem dos índices
del lanche[3]
lanche.pop(3)
lanche.remove('Pizza')
if 'Pizza' in lanche:
    lanche.remove('Pizza')  # remove só se tiver Pizza na lista
# Criar lista usando range
valores = list(range(4,11))
         # 4 5 6 7 8 9 10
# Índices: 0 1 2 3 4 5 6
val = [8, 2, 5, 4 ,9, 3, 0]
val.sort()  # Organiza em ordem
val.sort(reverse=True)  # Organiza ao contrário
