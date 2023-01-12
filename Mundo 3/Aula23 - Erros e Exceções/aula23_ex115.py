# Diretório: Exercícios_aula23
from Exercícios_aula23.lib.interface import *
from Exercícios_aula23.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

cabecalho('SISTEMA DE CADASTRO')
while True:
    opcao = menu(['Listar Pessoas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if opcao == 1:
        print('Listando Pessoas...'.center(42))
        sleep(1)
        lerArquivo(arq)
    elif opcao == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        print('\033[36mSaindo do Sistema', end='')
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.\033[m')
        sleep(1)
        print(linha())

        break
    else:
        print('\033[31mERRO! Opção inválida!\033[m')
    sleep(1)
