def criar_arquivo():
    with open('mensagem.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Olá mundo\n'
                      'Estou aprendendo python.\n'
                      'Estou estudando manipulação de arquivos.\n')

criar_arquivo()

def ler_arquivo():
    with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)


ler_arquivo()