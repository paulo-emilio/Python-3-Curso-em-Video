import random

num = random.random
print(num)
print(random.randint(1, 10))

# import Ctrl + espaço para ver exemplos
import opcode

# usar import's criados pela comunidade:
# exemplo: import emoji, clicar na lampada vermelha, clicar em instalar pacote -> Não funcionou
# modo que cosegui: configurações > Project:PythonProject > Python Interpreter

import emoji
print(emoji.emojize("earth_americas", use_aliases=True))

#Pessoal estamos na versão 3.10: tem umas alterações, lógico, mas ficou mais fácil como por exemplo
# os pacotes externos agora você acessa em um botão que fica bem abaixo na sua tela.
# Quando você apertar na package "emoji" vai aparecer um console explicando como colocar
# a entrada corretamente, por exemplo:
# print(emoji.emojize('ola, mundo!:globe_showing_Americas:', language='alias')).
# no exemplo ele colocou ":earth americas:" mas agora nessa
# versão s escreve ':globe_showing_Americas:', outra coisa é que agora (2022, v3.10)
# usamos 'language=alias' fiquem ligados o video é super atual mas o pycharm
# sempre atualiza tbm é so pesquisar um pouco.