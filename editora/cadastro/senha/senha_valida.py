def senha_valida():
    senha1 = input("Senha: ")
    senha2 = input("Insira a senha novamente: ")

    if senha1 == senha2:
        return senha1
    else:
        print("Senhas não correspondentes\nTente novamente!")
        senha_valida()
