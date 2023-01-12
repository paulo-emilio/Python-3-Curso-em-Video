print('\033[1;31;47mOlá, Mundo\033[m')
print('\033[7;30mOlá, Mundo\033[m')
a = 3
b = 5
print(f'Os valores são \033[35m{a}\033[m e\033[32m {b}\033[m')

nome = str(input('Seu nome para ficar colorido: '))
print('Olá, muito prazer em te conhecer, {}{}{}!'.format('\033[4;36m', nome, '\033[m'))

# Avançado
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'verde': '\033[32m',
         'preto_e_branco': '\033[7;30'}

print('Olá programador {}{}{}.'.format(cores['ciano'], nome, cores['limpa']))
