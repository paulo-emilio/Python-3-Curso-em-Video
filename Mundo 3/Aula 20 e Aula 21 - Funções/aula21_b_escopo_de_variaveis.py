def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()

# print(f'No programa principal, x vale {x}') -> Vai dar erro pq o x só foi definido dentro da def
print('=-'*50)


def funcao():
    n1 = 4
    n2 = 8
    print(f'n1 dentro vale {n1}')  # n1 aqui não mudará o valor do n1 global, mas sim criará uma variável
                                                                        # que ficará somente dentro da funcao
    print(f'n2 dentro vale {n2}')


n1 = 2
funcao()
print(f'n1 global vale {n1}')  # não será alterado com a função
# print(f'n2 global vale {n2}')  Dá erro pq não existe n2 global
print('=-'*50)


def func():
    global n  # avisa que é pra alterar sim no n global
    n = 8
    print(f'n dentro vale {n}')  # n aqui mudará o valor do n1 global


n = 2
print(f'n global vale {n}')
func()
print(f'n global vale {n}')  # será alterado após chamada a função
