# Python Console:
# help() > digitar um comando (ex: print) > obtém um manual sobre o comando
# quit para sair
# help(print()) -> Mostra a ajuda interativa também
# print(input.__doc__) -> Também faz isso
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: ínicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara
    """
    c = i
    while c <= f:
        print(f'{c} ', end='.. ')
        c += p
    print('Fim')


help(contador)
