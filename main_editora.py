from editora.inserts.insert_editora import inserir_autor, inserir_editora, inserir_genero, inserir_livro, inserir_cliente
from editora.cadastro.cadastro_cliente import cadastrar_cliente
from editora.login.login_ciente import logar_cliente
import os

nome_editora = 'Edicria'
print(f"Bem vido a {nome_editora}!")
print("Aqui registramos os seus livros para sua melhor visualização\n")
while True:
    print("Informe o que deseja fazer:\n")
    print("1 - Casdastro")
    print("2 - Login")
    print("3 - Sair\n")
    opc = (input())

    if opc == '1':
        os.system('cls' or 'clear')
        #função retorna toso os campos do cadastro
        cadastro_cliente = cadastrar_cliente()
    elif opc == '2':
        os.system('cls' or 'clear')
        #função booleana
        login_cliente = logar_cliente()

        if login_cliente:
            os.system('cls' or 'clear')
            print("Login realizado com sucesso!")
            input()
            #entra na editora
        else:
            os.system('cls' or 'clear')
            print("Login ou senha incorreta!")
            #volta pro loop do menu
    elif opc == '3':
        os.system('cls' or 'clear')
        print("Finalizando...")
        break
    else:
        os.system('cls' or 'clear')
        print("Valor inválido!")
        print("Tente novamente")
