print('Quantidade de tinta para pintar uma parede')
#Cada litro de tinta pinta 2m²

lar = float(input('Largura em metros: '))
alt = float(input('Altura em metros: '))
mquad = float(lar*alt)

print('Serão necessários', (mquad/2), 'litros de tinta')