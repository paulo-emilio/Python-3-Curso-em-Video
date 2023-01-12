# FATIAMENTO
#Usando a frase: Curso em Video Python
#frase[9] -> pega a décima letra da frase, pois começa a contar do zero
#frase[9:13] -> caractere 9 (que é a décima letra) ao caractere 12  (não conta com o último)
#frase[9:21:2] -> 9 ao 20 pulando de 2 em 2 (exemplo: video -> vdo)
#frase[:5] -> 0 ao 4
#frase[15:] -> 15 até o final
#frase[9::3] -> 9 até o final, pulando de 3 em 3 (Video Python -> VePh)

# ANÁLISE
#len(frase) -> pega o número de caracteres que tem na frase -> 21
#frase.count('o') -> pega quantas vezes aparece a letra "o" na frase
#frase.count('o',0,13) -> quantas letras "o" do caractere 0 ao caractere 12
#frase.find('deo') -> pega em qual caractere começa a sequência 'deo'
#frase.find('android') -> retorna: -1, significa que não foi encontrado
#'Curso' in frase -> vai retornar "True" pois existe essa sequencia de letras na frase

# TRANSFORMAÇÃO
#frase.replace('Python','Android') -> Substitui a sequencia "Python" por 'Android"
#frase.upper() -> Coloca tudo em letra maiúscula (CURSO EM VIDEO PYTHON)
#frase.lower() -> Coloca a frase toda em letra minúscula (curso em video python)
#frase.capitalize() -> Primeira letra maiúscula, resro minúscula (Curso em video python)
#frase.title() -> Todas iniciais das palavras maiusculas (Curso Em Video Python)
#frase.strip() -> remover todos espaços no início e no final das frases (caso o usuário saia apertando espaço atoa)
#frase.rstrip() -> remover somente os espaços do lado direito (últimos espaços)
#frase.lstrip() -> remover so os espaços da esquerda

# DIVISÃO DE STRINGS
#frase.split() -> Divide a frase considerando os espaços (cada palavra recebe indexação nova),
#[Curso] [em] [video] [Python] sendo que em [Curso] por exemplo, C==0 u==1 r==2 s==3 o==4, [em] e==0 m==1 ...
#   0      1     2        3   <-- Listas

# JUNÇÃO (Considerando que fez o split anterior)
#'-'.join(frase) -> junta a frase usando o separador indicado (Curso-em-Video-Python)
#' '.join(frase) ->                                           (Curso em video Python)




