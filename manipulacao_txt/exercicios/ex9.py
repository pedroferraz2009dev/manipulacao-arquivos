def numeros():
    with open('numeros.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('10\n'
                      '15\n'
                      '22\n'
                      '31\n'
                      '40\n'
                      '55\n'
                      '68\n'
                      '73\n'
                      '80\n'
                      '91\n')

numeros()

def mostrar_numeros():
    numeros = []

    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            numeros.append(int(linha.strip()))

    for numero in numeros:
        if numero % 2 == 0:
            print(numero)


mostrar_numeros()