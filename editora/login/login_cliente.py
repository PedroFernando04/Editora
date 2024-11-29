

def logar_cliente(conn):
    email = input("Login: ")
    senha = input("Senha: ")

    try:
        cursor = conn.cursor()
        query = "SELECT * FROM editora.clientes WHERE email_cliente = %s AND senha_cliente = %s"
        cursor.execute(query,(email, senha))
        conn.commit()
        row = cursor.fetchall()
    except Exception as e:
        print(f"ERRO: {e}")
    finally:
        cursor.close()
        conn.close()
    
    if row:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Usuário ou senha inválido!")
        return False

    
