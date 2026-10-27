def criar_arquivo():
    with open('nomes.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Pedro\n'
                      'Henrique\n'
                      'Stela\n'
                      'Marcia\n'
                      'Jeferson\n'
                      'Emília\n')

criar_arquivo()

def contar():
    quantidade = 0
    with open('nomes.txt', encoding='utf-8') as arquivo:
        for linha in arquivo:
            quantidade += 1
    print(f'Quantidade: {quantidade}')

contar()