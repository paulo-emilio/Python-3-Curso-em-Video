while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')

print('''\nAvacalha não. Só positivo por favor. 
Obs: Da pra fazer negativo também,mas
o exercício é esse, fazer o que.''')
