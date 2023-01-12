salario = float(input('Salário do funcionário: '))


if salario > 1250.00:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.15

print(f'Novo Salário {novo_salario :.2f}')
