def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos, VOTO FACULTATIVO'
    elif 0 <= idade < 16:
        return f'Com {idade} anos, VOTO NEGADO'
    elif idade < 0:
        return f'Veio do futuro? Não sei se você pode votar'
    else:
        return f'Com {idade} anos, VOTO OBRIGATÓRIO'


print(voto(int(input('Ano de Nascimento: '))))
