from editora.biblioteca.visualizar_livros import visualizar_livros
from editora.defs.defs_basicas import *
from editora.biblioteca.menus.menu_visualizar_livros_ano_lido import menu_visualizar_livros_ano_lido
from editora.biblioteca.menus.menu_visualizar_livros_nota import menu_visualizar_livros_nota

def menu_visualizar_livros(conn, id_cliente):
    while True:
        print("Informe como deseja visualizar os seus livros: ")
        print("\n1 - Todos\n2 - Filtrar pelo Status\n3 - Filtrar pelo ano lido\n4 - Filtrar pela nota\n5 - Voltar\n6 - Sair\n")
        valores_menu = {'1', '2', '3', '4'}

        menu = input()
        clear()

        cursor = conn.cursor()

        if menu == '1':
                query = """
                            SELECT nome_livro, nome_autor, nome_editora, 
                            data_de_lancamento_livro, nome_genero, nome_status, 
                            ano_lido_livro, nota_livro, resenha_livro
                            
                            FROM editora.livros l 
                            JOIN editora.autores a ON l.id_autor_livro = a.id_autor
                            JOIN editora.editoras e ON l.id_editora_livro = e.id_editora
                            JOIN editora.generos g ON l.id_genero_livro = g.id_genero
                            JOIN editora.status s ON l.id_status_livro = s.id_status

                            WHERE id_cliente_livro = %s
                        """
                
                cursor.execute(query, (id_cliente, ))
            
        elif menu == '2':
                    print("Escolha o status que deseja visualizar:")
                    print("\n1 - Lido\n2 - Lendo\n3 - Lista de Desejos\n")

                    menu_status = input()
                    clear()

                    query = """
                                SELECT nome_livro, nome_autor, nome_editora, 
                                data_de_lancamento_livro, nome_genero, nome_status, 
                                ano_lido_livro, nota_livro, resenha_livro
                                
                                FROM editora.livros l 
                                JOIN editora.autores a ON l.id_autor_livro = a.id_autor
                                JOIN editora.editoras e ON l.id_editora_livro = e.id_editora
                                JOIN editora.generos g ON l.id_genero_livro = g.id_genero
                                JOIN editora.status s ON l.id_status_livro = s.id_status

                                WHERE id_cliente_livro = %s and id_status_livro = %s
                            """
                    cursor.execute(query, (id_cliente, menu_status))
                    
        elif menu == '3':
                    menu_visualizar_livros_ano_lido(cursor, id_cliente)

        elif menu == '4':
                    menu_visualizar_livros_nota(cursor, id_cliente)
                    
        elif menu == '5':
                    break
        elif menu == '6':
                    print("\nFinalizando...")
                    exit()
        else:
                print("Valor inválido!\n")
                delay()


        if menu in valores_menu:
                livros = cursor.fetchall()

                visualizar_livros(livros)
                delay()
        else: 
            continue            
            
