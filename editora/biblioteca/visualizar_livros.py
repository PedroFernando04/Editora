
def visualizar_livros(conn, id_cliente):
    
    cursor = conn.cursor()
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
    cursor.execute(query, (id_cliente,))
    livros = cursor.fetchall()

    for livro in livros:
        info_livro = (
            livro[0],
            livro[1],
            livro[2],
            livro[3],
            livro[4],
            livro[5],
            livro[6],
            livro[7],
            livro[8]
        )

        (nome, autor, editora, data_lancamento, genero,  status, ano_lido, nota, resenha) = info_livro
        
        print("-"*120)
        print(f"Nome: {nome}")
        print(f"Autor(a): {autor}")
        print(f"Editora: {editora}")
        print(f"Data de Lançamento: {data_lancamento}")
        print(f"Gênero: {genero}")
        print(f"Status: {status}")
        print(f"Ano lido: {ano_lido}")
        print(f"Nota: {nota}")
        print(f"Resenha: {resenha}")
        print("-"*120)
