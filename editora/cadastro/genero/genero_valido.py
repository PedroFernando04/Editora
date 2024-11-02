import os

def genero_valido():
    print("M - Masculino\nF - Feminino\nI - Indefinido")
    genero = input("\nGenero: ").upper()
    while True:
        if genero not in ['M', 'F', 'I']:
            os.system('cls' or 'clear')
            print("Valor inválido!")
            print("Informe seu gênero seguindo a tabela\n")

            print("M - Masculino\nF - Feminino\nI - Indefinido")
            genero = input("\nGenero: ").upper()
            os.system('cls' or 'clear')
        else:
            os.system('cls' or 'clear')
            print("Genero cadastrado com sucesso!")
            return genero
