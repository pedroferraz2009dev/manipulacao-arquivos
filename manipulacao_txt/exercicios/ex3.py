def adicionar():
    frase_adicionada = input("Digite uma frase: ")
    with open("frase.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(frase_adicionada + "\n")

        print("frase adicionada")

adicionar()
