from editora.inserts.insert_editora import inserir_autor, inserir_editora, inserir_genero, inserir_livro, inserir_cliente
from editora.cadastro.cadastro_cliente import cadastrar_cliente
from editora.login.login_cliente import logar_cliente
from editora.conexao.criar_conexao_editora import conexao
from editora.biblioteca.menu_editora import menu_editora

from editora.defs.defs_basicas import *

conn = conexao()

clear()
nome_editora = 'Edicria'
print(f"Bem vido a {nome_editora}!")
print("Aqui registramos os seus livros para sua melhor visualização\n")
while True:
    print("Informe o que deseja fazer:\n")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair\n")
    opc = (input())
    clear()

    if opc == '1':
        #função retorna toso os campos do cadastro
        cadastro_cliente = cadastrar_cliente(conn)
    elif opc == '2':
        
        #função booleana
        id_cliente = logar_cliente(conn)

        if id_cliente:
            delay()
            #entra na editora
            menu_editora(conn, id_cliente)
        else:
            delay()
            #volta pro loop do menu

    elif opc == '3':
        print("Finalizando...")
        break

    else:
        print("Valor inválido!")
        print("Tente novamente")

conn.close()
