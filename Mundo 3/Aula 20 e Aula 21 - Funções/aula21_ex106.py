import time


def helping(h):
    print(f'\033[7mAcessando o Manual do comando {h}\033[m')
    print('\033[36m', end='')
    time.sleep(1)
    help(h)
    print('\033[m')
    time.sleep(1)


rsp = ''
while True:
    print('\033[42;30m', end='')
    print('\033[42mSistema de Ajuda PyHelp\033[m')
    rsp = input('Função ou Biblioteca -> ')
    if rsp.upper() != 'FIM':
        helping(rsp)
    else:
        print('\033[35mOk, bye!\033[m')
        break
