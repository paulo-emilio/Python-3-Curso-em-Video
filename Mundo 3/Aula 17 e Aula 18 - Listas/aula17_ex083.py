exp = input('Digite uma expressão: ').strip()
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('x')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append('x')
            break
if len(pilha) == 0:
    print('Okay')
else:
    print('Wrong')
