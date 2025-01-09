def logar_cliente(conn):
    email = input("Login: ")
    senha = input("Senha: ")

    try:
        cursor = conn.cursor()
        query = "SELECT id_cliente FROM editora.clientes WHERE email_cliente = %s AND senha_cliente = %s"
        cursor.execute(query,(email, senha))
        conn.commit()
        row = cursor.fetchone()
    except Exception as e:
        print(f"ERRO: {e}")
    
    if row:
        print("\nLogin realizado com sucesso!\n")
        return row
    else:
        print("\nUsuário ou senha inválido!")
        return False
