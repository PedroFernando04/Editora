import os

def senha_valida():
    senha1 = input("Senha: ")
    senha2 = input("Insira a senha novamente: ")
    while True:
        if senha1 == senha2:
            print("Senha cadastrada!")
            return senha1
        else:
            os.system('cls' or 'clear')
            print("Senhas não correspondentes\nTente novamente!\n")
            senha1 = input("Senha: ")
            senha2 = input("Insira a senha novamente: ")
            os.system('cls' or 'clear')
            
    
def mostrar_senha(senha):
    for i in range (0, len(senha)):
        print('*', end = " ")
    print("")
