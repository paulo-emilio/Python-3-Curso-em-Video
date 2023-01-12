for c in range(1, 6):  # REPETINDO 5 VEZES
    print('Oi', c)
print('FIM')

for c in range(6, 0, -1):  # REPETINDO 5 VEZES DE TRÁS PARA FRENTE
    print('Oi', c)

for c in range(0, 7, 2):  # PULANDO 2 EM 2
    print(c)


n = int(input('Vamos contar até este número: '))
for c in range (0, n + 1):
    print(c)

# Colocando início, fim e de quantos em quantos vai pular
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)

# Pedindo mesmo input várias vezes
s = 0
for c in range(0, 5):
    n = int(input('Digite um número para somar: '))
    s += n  # (s = s + n)
print(f'A soma de todos foi: {s}')
