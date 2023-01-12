aluno = {'Nome': input('Nome: ').capitalize().strip()}
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
print('-'*30)
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovad@'
else:
    aluno['Situação'] = 'Reprovad@'
for k, v in aluno.items():
    x = ''
    print(f'  * {k}: {v}')
    