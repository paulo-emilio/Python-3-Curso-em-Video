frase = 'Curso em Vídeo Python'
print(frase)
print(frase[15])
print(frase[9:])
print(frase[6:11])
print(frase[:14])
print(frase[2:15:2])
print(frase[::3],'\n')

print(frase.count('o')) #conta somente o's minusculos
print(frase.upper().count('Y')) #passando tudo pra maiúsculo e contando qnts Y's
print(len(frase),'\n')

frase = '    Curso em Vídeo Python     ' #Vários espaços dos lados
print(len(frase)) #lê com os espaços
print(len(frase.strip()),'\n') #corta os espaços sobrando dos lados

print(frase.strip().replace('Python', 'C#'),'\n') #substitui a sequência Python por C#

frase.replace('Curso', 'Aula') #subtitui somente nessa instânica, não salva no banco
print(frase)
frase = frase.replace('Curso', 'Aula') #"frase =" alterando o valor de "frase"
print(frase, '\n')

print(frase.find('Python')) #procura a sequência de letras e mostra a posição que ela começa
print(frase.find('python')) #não acha pq o P é maiusculo (resultado: -1)
print(frase.lower().find('python'),'\n') #acha pois a frase foi toda jogada pra minusculo

#split
dividido = frase.split()
print(dividido)
print(dividido[0]) #pega a palavra que está no 0
print(dividido[3][1]) #pega a letra que está no 1 da palavra 3
print(dividido[0],dividido[3]) #palavra 0 e 3

print('\n')

print('''O Curso de Segurança da Informação vai
ensinar os fundamentos para uma vida mais segura
no mundo digital. Ultimamente estamos presenciando
muitas tentativas de fraude e invasões a sistemas,
nosso objetivo é esclarecer as principais dúvidas
da área. Neste curso, os professores Alfredo Júnior
e Gustavo Guanabara criaram um conjunto de vídeos que
vão analisar o conteúdo da cartilha de segurança do 
CERT.br. ''')