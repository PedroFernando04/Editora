from editora.biblioteca.cadastrar_livros import cadastro_livro
from editora.biblioteca.menus.menu_visualizar_livros import menu_visualizar_livros
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
                clear()

                autor = cadastro_livro.autor_livro(conn)
                clear()

                editora = cadastro_livro.editora_livro(conn)
                clear()

                data = cadastro_livro.data_livro()
                clear()

                genero = cadastro_livro.genero_livro(conn)
                clear()

                status = cadastro_livro.status_livro(conn)
                clear()

                if status == '1':
                    ano = cadastro_livro.ano_lido_livro(ano_atual = 2025)
                    clear()

                    nota = cadastro_livro.nota_livro()
                    clear()

                    resenha = cadastro_livro.resenha_livro()
                    clear()
                else:
                    ano = nota = resenha = 'null'

                inserir_livro(conn, nome, autor, editora, data, genero, status, ano, nota, resenha, id_cliente)
            
            case '2':
                menu_visualizar_livros(conn, id_cliente)
            
            case '3':
                continue
                #update livro
            
            case '4':
                print("Finalizando...")
                exit()
            
            case _:
                print("Valor inválido!\n")
