from editora.biblioteca.cadastrar_livros import cadastro_livro
from editora.biblioteca.visualizar_livros import visualizar_livros
from editora.inserts.insert_editora import inserir_livro
from editora.defs.defs_basicas import *


def menu_editora(conn, id_cliente):
    while True:
        print("Informe o que deseja fazer:\n")
        print("1 - Cadastrar livro")
        print("2 - Visualizar livros")
        print("3 - Alterar livro")
        print("4 - Sair\n")
        opc = (input())
        clear()

        match(opc):
            case '1':
                cadastro_livro.__init__()
                nome = cadastro_livro.nome_livro(conn)
                autor = cadastro_livro.autor_livro(conn)
                editora = cadastro_livro.editora_livro(conn)
                data = cadastro_livro.data_livro()
                genero = cadastro_livro.genero_livro(conn)
                status = cadastro_livro.status_livro(conn)
                ano = cadastro_livro.ano_lido_livro(ano_atual = 2024)
                nota = cadastro_livro.nota_livro()
                resenha = cadastro_livro.resenha_livro()

                inserir_livro(conn, nome, autor, editora, data, genero, status, ano, nota, resenha, id_cliente)
            
            case '2':
                visualizar_livros(conn, id_cliente)
                delay()
            
            case '3':
                continue
                #update livro
            
            case '4':
                print("Finalizando...")
                exit()
            
            case _:
                print("Valor inválido!\n")
