from editora.defs.defs_basicas import *

def genero_valido():
    print("M - Masculino\nF - Feminino\nI - Indefinido")
    genero = input("\nGenero: ").upper()
    while True:
        if genero not in ['M', 'F', 'I']:
            clear()
            print("Valor inválido!")
            print("Informe seu gênero seguindo a tabela\n")

            print("M - Masculino\nF - Feminino\nI - Indefinido")
            genero = input("\nGenero: ").upper()
            clear()
        else:
            clear()
            print("Genero cadastrado com sucesso!")
            return genero
