somaidade = 0
mediaidade = 0
idadevelhoh = 0
nomevelhoh = ''
mulheresmenos20 = 0

for c in range(1, 5):
    print(f'--- {c}ª PESSOA ---')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    # Média idades
    somaidade += idade
    mediaidade = somaidade / c
    # Homem mais velho
    if sexo == 'M' and idade > idadevelhoh:  # Poderia usar 'sexo in 'Mm' para nao precisar usar o upper
        idadevelhoh = idade
        nomevelhoh = nome
    # Mulheres menos de 20
    if sexo in 'Ff' and idade < 20:
        mulheresmenos20 += + 1


print(f'A média de idade do grupo é de: {mediaidade} anos.')
print(f'O homem mais velho tem {idadevelhoh} anos e se chama {nomevelhoh}.')
print(f'Ao todo são {mulheresmenos20} mulher(es) com menos de 20 anos.')
