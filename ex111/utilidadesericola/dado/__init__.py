def leiaDinheiro(v):
    while True:
        entrada = str(input(v)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO! "{entrada}" não é um preço válido!\033[m')
        else:
            return float(entrada)
