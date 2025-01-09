from editora.defs.defs_basicas import *

def menu_visualizar_livros_nota(cursor, id_cliente):
    print("Como deseja filtrar:")
    print("\n1 - Crescente\n2 - Decrescente\n3 - Escolher nota\n")

    menu_nota = input()
    clear()

    #CRESCENTE
    if menu_nota == '1':
        query = """
                    SELECT nome_livro, nome_autor, nome_editora, 
                    data_de_lancamento_livro, nome_genero, nome_status, 
                    ano_lido_livro, nota_livro, resenha_livro
                    
                    FROM editora.livros l 
                    JOIN editora.autores a ON l.id_autor_livro = a.id_autor
                    JOIN editora.editoras e ON l.id_editora_livro = e.id_editora
                    JOIN editora.generos g ON l.id_genero_livro = g.id_genero
                    JOIN editora.status s ON l.id_status_livro = s.id_status

                    WHERE id_cliente_livro = %s AND id_status_livro = 1
                    ORDER BY nota_livro
                """
        cursor.execute(query, (id_cliente, ))
        
    #DECRESCENTE
    elif menu_nota == '2':
        query = """
                    SELECT nome_livro, nome_autor, nome_editora, 
                    data_de_lancamento_livro, nome_genero, nome_status, 
                    ano_lido_livro, nota_livro, resenha_livro
                    
                    FROM editora.livros l 
                    JOIN editora.autores a ON l.id_autor_livro = a.id_autor
                    JOIN editora.editoras e ON l.id_editora_livro = e.id_editora
                    JOIN editora.generos g ON l.id_genero_livro = g.id_genero
                    JOIN editora.status s ON l.id_status_livro = s.id_status

                    WHERE id_cliente_livro = %s AND id_status_livro = 1
                    ORDER BY nota_livro DESC
                """ 
        cursor.execute(query, (id_cliente, ))
        
    elif menu_nota == '3':

        query_nota = """
                        SELECT DISTINCT nota_livro
                        
                        FROM editora.livros l
                            
                        WHERE id_cliente_livro = %s AND id_status_livro = 1
                    """
        cursor.execute(query_nota, (id_cliente, ))

        notas = cursor.fetchall()

        while True:
            print("Selecione a nota:\n")

            for i in range(0, len(notas)):
                print(f"{i + 1} - {notas[i][0]}")
            
            try:
                nota = int(input("\n"))

                if nota not in range(1, len(notas) + 1):
                    raise Exception

                clear()
                
            except:
                clear()
                print("Valor inválido!")
                print("Digite um número presente na tabela\n")

            else:
                break
            
            if nota > 0 and nota <= len(notas):
                break
            else:
                continue

        
        query = """
                    SELECT nome_livro, nome_autor, nome_editora, 
                    data_de_lancamento_livro, nome_genero, nome_status, 
                    ano_lido_livro, nota_livro, resenha_livro
                    
                    FROM editora.livros l 
                    JOIN editora.autores a ON l.id_autor_livro = a.id_autor
                    JOIN editora.editoras e ON l.id_editora_livro = e.id_editora
                    JOIN editora.generos g ON l.id_genero_livro = g.id_genero
                    JOIN editora.status s ON l.id_status_livro = s.id_status

                    WHERE id_cliente_livro = %s AND nota_livro = %s AND id_status_livro = 1
                """ 
        cursor.execute(query, (id_cliente, notas[nota - 1][0]))
    
