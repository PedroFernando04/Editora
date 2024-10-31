from editora.criar_conexao_editora import conexao

def inserir_autor(nome, data, genero):
    conn = conexao()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO autores(nome_autor, data_nascimento, genero_autor) VALUES (%s, %s, %s);"
        cursor.execute(query, (nome, data, genero))
        conn.commit()
        print("Autor cadastrado com sucesso!")
    except Exception as e:
        print(f"ERRO AUTOR: {e}")
    finally:
        cursor.close()
        conn.close()

def inserir_editora(nome):
    conn = conexao()
    try:
        cursor= conn.cursor()
        query = "INSERT INTO editoras(nome_editora) VALUES (%s);"
        cursor.execute(query, (nome,))
        conn.commit()
        print(f"Editora cadastrada com sucesso!")
    except Exception as e:
        print(f"ERRO EDITORA: {e}")
    finally:    
        cursor.close()
        conn.close()

def inserir_genero(nome):
    conn = conexao()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO generos(nome_genero) VALUES (%s);"
        cursor.execute(query, (nome,))
        conn.commit()
        print("Genero cadastrado com sucesso!")
    except Exception as e:
        print(f"ERRO GENERO: {e}")
    finally:
        cursor.close()
        conn.close()

def inserir_livro(nome, id_autor, id_editora, data, id_genero):
    conn = conexao()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO livros(nome_livro, id_autor_livro, id_editora_livro, data_de_lancamento, id_genero_livro) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, (nome, id_autor, id_editora, data, id_genero))
        conn.commit()
        print("Livro cadastrado com sucesso!")
    except Exception as e:
        print(f"ERRO LIVRO: {e}")
    finally:
        cursor.close()
        conn.close()
