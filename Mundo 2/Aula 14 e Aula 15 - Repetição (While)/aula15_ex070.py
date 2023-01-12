print('=-'*10)
print('LOJA PRECIN DA HORA')
print('=-'*10)

tot = maismil = barato = cont = 0
baratonome = ' '

while True:
    nome = input('Nome do produto: ').strip().capitalize()
    preco = float(input('Preço: R$ '))
    if preco > 1000:
        maismil += 1
    tot += preco
    cont += 1
    if cont == 1 or preco < barato:
        barato = preco
        baratonome = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Mais? [S/N]: ').upper().strip()[0]
    if continuar in 'S':
        print('=-'*10)
    elif continuar in 'Nn':
        break

print(f'O total da compra foi: R$ {tot:.2f}')
print(f'Temos {maismil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {baratonome} que custa R$ {barato:.2f}')