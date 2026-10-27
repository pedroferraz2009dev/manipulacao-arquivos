def alunos():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        arquivo.write('Ana;8.5\n'
                      'Bruno;5.0\n'
                      'Carlos;7.2\n'
                      'Daniela;9.0\n'
                      'Eduardo;4.5\n'
                      'Fernando;6.8\n'
                      'Gabriel;5.9\n')

alunos()

def listar_aprovados():
    print("Alunos aprovados:")

    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")
            nota = float(nota)

            if nota >= 6:
                print(f"{nome} - {nota}")


listar_aprovados()