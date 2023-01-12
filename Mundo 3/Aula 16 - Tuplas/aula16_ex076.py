
listagem = ('Processador', 999.99,
            'Cooler', 300.00,
            'Placa Mãe', 555.55,
            'Placa de Vídeo', 2222.22,
            'Monitor', 1300.00,
            'Teclado e Mouse', 199.99,
            'Memória RAM', 300.00,
            'Fonte', 500.00)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    elif pos % 2 == 1:
        print(f'R$ {listagem[pos]:>7.2f}')
print('-'*40)