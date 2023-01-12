# {:.2f} no .format mostra somente 2 casas depois da vírgula

# Ctrl + espaço dá exemplos do que pode ser escrito (ex: import Ctrl + espaço)

# Todo método precisa de ()

# Imprimindo o texto "pre configurado"

print('''O Curso de Segurança da Informação vai
ensinar os fundamentos para uma vida mais segura
no mundo digital. Ultimamente estamos presenciando
muitas tentativas de fraude e invasões a sistemas,
nosso objetivo é esclarecer as principais dúvidas
da área. Neste curso, os professores Alfredo Júnior
e Gustavo Guanabara criaram um conjunto de vídeos que
vão analisar o conteúdo da cartilha de segurança do 
CERT.br. ''')

# O .format a partir da versão 3 do Python pode ser usado assim:
#print(f"Olá, {nome}, você está com {idade} anos de idade correto?")

nome = 'Paulo'
idade = 22
salario = 1200.0
# 20 espaços e centralizado (^)
print(f'{nome:^20} tem {idade} anos, e ganha R${salario:.2f} por mês.')

# 20 (-) e centralizado (^)
print(f'{nome:-^20} tem {idade} anos, e ganha R${salario:.2f} por mês.')

# 20 (-) e alinha a direita (>)
print(f'{nome:->20} tem {idade} anos, e ganha R${salario:.2f} por mês.')

print('Centro'.center(42))  # Centraliza dependendo do número colocado
