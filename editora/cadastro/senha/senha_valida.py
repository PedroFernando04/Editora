from editora.defs.defs_basicas import *

def senha_valida():
    senha1 = input("Senha: ")
    senha2 = input("Insira a senha novamente: ")
    while True:
        if senha1 == senha2:
            print("Senha cadastrada!")
            return senha1
        else:
            clear()
            print("Senhas não correspondentes\nTente novamente!\n")
            senha1 = input("Senha: ")
            senha2 = input("Insira a senha novamente: ")
            clear()
            
    
def mostrar_senha(senha):
    for i in range (0, len(senha)):
        print('*', end = " ")
    print("")
