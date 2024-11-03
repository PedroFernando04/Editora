from editora.conexao.criar_conexao_editora import conexao

def inserir_autor(nome, data, genero, pais):
    conn = conexao()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO autores(nome_autor, data_nascimento, genero_autor, pais_autor) VALUES (%s, %s, %s, %s);"
        cursor.execute(query, (nome, data, genero, pais))
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

def inserir_cliente(nome, email, senha, genero, pais, data):
    conn = conexao()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO clientes(nome_cliente, email_cliente, senha_cliente, genero_cliente, pais_cliente, data_nascimento_cliente) VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (nome, email, senha, genero, pais, data))
        conn.commit()
        print("Usuario cadastrado com sucesso!")
    except Exception as e:
        print(f"ERRO CLIENTE: {e}")
    finally:
        cursor.close()
        conn.close()

def inserir_livro(nome, id_autor, id_editora, data, id_genero, status, ano, nota, resenha, id_cliente):
    conn = conexao()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO livros(nome_livro, id_autor_livro, id_editora_livro, data_de_lancamento, id_genero_livro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (nome, id_autor, id_editora, data, id_genero, status, ano, nota, resenha, id_cliente))
        conn.commit()
        print("Livro cadastrado com sucesso!")
    except Exception as e:
        print(f"ERRO LIVRO: {e}")
    finally:
        cursor.close()
        conn.close()
