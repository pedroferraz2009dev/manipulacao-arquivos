# Modo "r" - Abre o arquivo para leitura
# Modo "w" - Abre para escrita e apaga conteúdo existente
# Modo "a" - Adiciona novo conteúdo no final do projeto
# Modo "x" - Cria arquivo novo e gera erro se ele ja existir

def criar_arquivo_txt():
    # O "with" fecha o arquivo automaticamente
    # O "open()" função para leitura ou escrita de arquivos
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Pedrolindo\n")
        arquivo.write("Henriquelindo\n")
        arquivo.write("Ferrazlindo\n")

criar_arquivo_txt()

def adicionar_aluno(nome):
    with open("alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome)

# adicionar_aluno("Pedrobonito")
# adicionar_aluno("Henriquebonito")
# adicionar_aluno("Ferrazbonito")

def listar_alunos():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print(f"O conteúdo do arquivo alunos é {conteudo}")

# listar_alunos()

def listar_aluno_individual():
    lista_alunos = []
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:

        print(f"Lista de alunos: {lista_alunos}")

# listar_aluno_individual()


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    with open("alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{idade}\n")

    print('Aluno cadastrado com sucesso!')

# cadastrar_aluno()

def listar_cadastro():
    item_cadastro = []
    with (open("alunos.txt", "r", encoding="utf-8") as arquivo):
        for linha in arquivo:
            nome, idade = linha.strip().split(";")

            obj = {
                "nome": nome,
                "idade": idade
            }
            item_cadastro.append(obj)
    print(f"itens cadastrados: {item_cadastro}")

listar_cadastro()