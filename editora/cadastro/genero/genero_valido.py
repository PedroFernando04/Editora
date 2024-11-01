def genero_valido():
    while True:
        print("M - Masculino\nF - Feminino\nI - Indefinido")
        genero = input("\nGenero: ").upper()
        if genero not in ['M', 'F', 'I']:
            print("\nValor inválido!")
            print("Informe seu gênero seguindo a tabela\n")
        else:
            print("\nGenero cadastrado com sucesso!")
            return genero
