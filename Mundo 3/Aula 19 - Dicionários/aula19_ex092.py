from datetime import datetime
trabalhador = {'Nome': input('Nome: ').capitalize().strip(),
               'Idade': datetime.now().year - int(input('Ano de Nascimento: ').strip()),
               'CTPS': int(input('Carteira de Trabalho [0 - Não possui]: ').strip())
               }
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de Contratação: ').strip())
    trabalhador['Salário'] = float(input('Salário: ').strip())
    trabalhador['Aposentadoria'] = ((trabalhador['Contratação'] + 35) - datetime.now().year + trabalhador['Idade'])
    for k, v in trabalhador.items():
        print(f'  * {k}: {v}')

else:
    print('=-'*20)
    del trabalhador['CTPS']
    for k, v in trabalhador.items():
        print(f'  * {k}: {v}')
        print('  * Não possui carteira de trabalho')
