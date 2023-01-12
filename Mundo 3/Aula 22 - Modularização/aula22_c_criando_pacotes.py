# Pacote criado a partir da pasta inicial (pythonProject)
# Dentro de um pacote podem ser criados mais pacotes
# Para essa aula foi criado o pacote uteis e dentro dele, pacotes como: numeros, strings, datas...

from aula22_c_uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat} :D '
      f'\nIMPORTADO COM SUCESSO!')
