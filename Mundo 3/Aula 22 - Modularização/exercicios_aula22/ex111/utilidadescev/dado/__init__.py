def leiaDinheiro(valor):
    while True:
        entrada = input(valor).strip().replace(',', '.').replace(' ', '')
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! "{entrada}" não é um preço.')
        else:
            return float(entrada)
