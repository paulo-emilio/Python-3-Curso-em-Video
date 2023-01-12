pessoa = {}
todaspessoas = []
mulheres = []
rsp = ''
somaidades = 0

while True:
    pessoa['Nome'] = input('Nome: ').strip().capitalize()
    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
        if sexo in 'MF':
            pessoa['Sexo'] = sexo
            if sexo == 'F':  # add a lista mulheres
                mulheres.append(pessoa['Nome'])
            break

        else:
            print('Somente M (masculino) ou F (feminino)')

    pessoa['Idade'] = int(input('Idade: ').strip())
    somaidades += pessoa['Idade']  # soma idades
    todaspessoas.append(pessoa.copy())  # coloca pessoa em todas pessoas
    print(pessoa)
    pessoa.clear()  # apaga pessoa
    while True:
        rsp = input('Continuar? [S/N]: ').strip().upper()[0]
        if rsp == 'N':
            break
        elif rsp == 'S':
            break
        else:
            print('Somente S (sim) ou N (não)')
    if rsp == 'N':
        break
print('=-'*25)

print(f'A) Ao todo temos {len(todaspessoas)} pessoas cadastradas.')
# media de idades
mediaidades = somaidades/len(todaspessoas)
print(f'B) A média de idade é de {mediaidades:.2f} anos')
print(f'C) As mulheres cadastradas foram {mulheres}')
print('D) Lista de pessoas acima da média de idade:', end='')
for p in todaspessoas:
    if p['Idade'] >= mediaidades:
        print('    ')
        for k, v in p.items():
            print(f'   {k}: {v}; ', end='')
