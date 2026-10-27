import csv

def criar_csv():
    with open("alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerow(["Pedro", 17, "Futebol"])
        escritor.writerow(["Henrique", 18, "Corinthians"])
        escritor.writerow(["Ferraz", 19, "Yuri Alberto"])

#criar_csv()

def salvar_alunos():
    alunos = [
        ["Pedro", 17, "Futebol"],
        ["Henrique", 18, "Corinthians"],
        ["Ferraz", 19, "Yuri Alberto"],
        ["Silva", 20, "Neymar"],
        ["Stela", 21, "Mavie"],
        ["Maria", 22, "Mel"]
    ]

    with open("novos_alunos.csv", "w", newline="", encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerows(alunos)

#salvar_alunos()

def ler_csv():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)

        for linha in leitor:
            print(linha[0])

#ler_csv()

def exibir_alunos():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        alunos = csv.DictReader(arquivo)

        for aluno in alunos:
            print(aluno)

#exibir_alunos()


def cadastrar_alunos():
    with open("novos_alunos.csv", "a+", encoding="utf-8") as arquivo:
        #Move o cursor para o final do arquivo
        arquivo.seek(0,2)
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite o idade do aluno: "))
        curso = input("Digite o curso do aluno: ")

        escritor = csv.writer(arquivo)
        escritor.writerow([nome, idade, curso])

        #Move o cursor para o inicio do arquivo
        arquivo.seek(0,2)
        leitor = csv.DictReader(arquivo)

        for aluno in leitor:
            print(linha)

cadastrar_alunos()

def deletar_alunos():

    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        alunos = list(leitor)

    with open("novos_alunos.csv", "w", encoding="utf-8") as arquivo:
        cabecalho = ["Nome", "Idade", "Curso"]
        escritor = csv.writer(arquivo, fieldnames=cabecalho)

        escritor.writeheader()

        alunos_apagar = input("Digite o nome do aluno que deseja apagar: ")

        for aluno in alunos:
            if aluno["Nome"] != alunos_apagar:
                escritor.writerow(aluno)

deletar_alunos()