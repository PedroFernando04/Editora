def inserir_autor(conn, nome, data, genero, pais):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO editora.autores(nome_autor, data_nascimento_autor, genero_autor, pais_autor) VALUES (%s, %s, %s, %s);"
        cursor.execute(query, (nome, data, genero, pais))
        conn.commit()
        print("Autor cadastrado com sucesso!")
    except Exception as e:
        print(f"ERRO AUTOR: {e}")
    

def inserir_editora(conn, nome):
    try:
        cursor= conn.cursor()
        query = "INSERT INTO editora.editoras(nome_editora) VALUES (%s);"
        cursor.execute(query, (nome,))
        conn.commit()
        print(f"Editora cadastrada com sucesso!")
    except Exception as e:
        print(f"ERRO EDITORA: {e}")
    

def inserir_genero(conn, nome):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO editora.generos(nome_genero) VALUES (%s);"
        cursor.execute(query, (nome,))
        conn.commit()
        print("Genero cadastrado com sucesso!")
    except Exception as e:
        print(f"ERRO GENERO: {e}")

def inserir_cliente(conn, nome, email, senha, genero, pais, data):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO editora.clientes(nome_cliente, email_cliente, senha_cliente, genero_cliente, pais_cliente, data_nascimento_cliente) VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (nome, email, senha, genero, pais, data))
        conn.commit()
        print("Usuario cadastrado com sucesso!")
    except Exception as e:
        print(f"ERRO CLIENTE: {e}")

def inserir_livro(conn, nome, id_autor, id_editora, data, id_genero, status, ano, nota, resenha, id_cliente):
    try:
        cursor = conn.cursor()
        if status == 1:
            query = "INSERT INTO editora.livros(nome_livro, id_autor_livro, id_editora_livro, data_de_lancamento_livro, id_genero_livro, id_status_livro, ano_lido_livro, nota_livro, resenha_livro, id_cliente_livro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(query, (nome, id_autor, id_editora, data, id_genero, status, ano, nota, resenha, id_cliente))
        
        else:
            query = "INSERT INTO editora.livros(nome_livro, id_autor_livro, id_editora_livro, data_de_lancamento_livro, id_genero_livro, id_cliente_livro) VALUES (%s, %s, %s, %s, %s, %s, %s);" 
            cursor.execute(query, (nome, id_autor, id_editora, data, id_genero, status, id_cliente))
        
        conn.commit()
        print("Livro cadastrado com sucesso!")
    except Exception as e:
        print(f"ERRO LIVRO: {e}")

