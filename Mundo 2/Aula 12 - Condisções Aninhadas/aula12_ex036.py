print('Vamos ver se seu empréstimo pode ser aprovado.')
valor = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Em quantos anos você quer pagar? '))
prestacao = valor / (anos * 12)

print(f'A prestação mensal ficará em {prestacao:.2f}')

if prestacao <= 0.3 * salario:
    print('Você pode fazer o empréstimo!!!')
else:
    print('Infelizmente você não pode fazer o empréstimo. :(')