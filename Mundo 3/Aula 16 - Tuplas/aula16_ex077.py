palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRÁTIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR'
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for l in p:
        if l in 'AÁÂÃÀEÉÉÊÍÌÎIOÓÒÕÔÚÙÛU':
            print(l, end='')