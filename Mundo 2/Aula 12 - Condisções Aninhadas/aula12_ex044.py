print('Descobrir preço Final')
print('-------------------------')
preco = float(input('Preço das compras R$ : '))
final_preco = float()
print('-------------------------')
condicao = int(input('''[ 0 ] À vista - Dinheiro / Cheque (-10%)
[ 1 ] À vista - Cartão (-5%)
[ 2 ] 2x no Cartão
[ 3 ] 3x ou mais no Cartão (+20%)

Condição de pagamento: '''))
print('-------------------------')

if condicao == 0:
    final_preco = preco * 0.9
elif condicao == 1:
    final_preco = preco * 0.95
elif condicao == 2:
    final_preco = preco
    print('A compra será parcelada em 2x.')
elif condicao == 3:
    final_preco = preco * 1.2
    parcelas = int(input('Quantas parcelas: '))
    print(f'A compra será parcelada em {parcelas}x com Juros de 20%.')
else:
    print('Digita direito sua mula!')

print(f'Preço final: {final_preco:.2f}')
