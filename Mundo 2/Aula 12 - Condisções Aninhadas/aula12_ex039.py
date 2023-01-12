from datetime import date

print('Você deve se alistar?')
nascimento_ano = int(input('Ano de Nascimento: '))
atual_ano = date.today().year
idade = atual_ano - nascimento_ano

if nascimento_ano > atual_ano:
    print('Você veio do futuro! Desculpe, não sei te falar se pode se alistar.')
else:
    print(f'Você fez/faz {idade} anos esse ano.')
    sexo = int(input('''--------------------------------
[ 1 ] Masculino
[ 2 ] Feminino
Seu sexo: '''))

    if sexo == 1:
        if idade < 18:
            print(f'Você ainda não pode se alistar. Poderá daqui {18 - idade} anos.')
            print(f'Seu alistamento será em {atual_ano + (18 - idade)}.')

        elif idade == 18:
            print('Está na sua hora!')

        elif 18 < idade <= 45:
            print(f'Já passaram {idade - 18} anos da sua hora de alistar.')
            print(f'''Você deveria ter se alistado em {atual_ano - (idade - 18)}.
Como você tem menos de 45 ainda deve se alistar.''')

        elif idade > 45:
            print('Você já tem mais de 45, não precisa mais se alistar')
            print(f'Já passaram {idade - 18} anos da sua hora de alistar.')

    else:
        print('Como você é do sexo feminino, não é obrigatório seu alistamento.')