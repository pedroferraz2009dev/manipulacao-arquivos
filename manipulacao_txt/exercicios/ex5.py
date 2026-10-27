def texto():
    with open('texto.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Python\n')

texto()

def contar_caracteres():
    with open('texto.txt', 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
    quantidade = len(texto)

    print(f'Quantidade de caracteres é: {quantidade}')

contar_caracteres()