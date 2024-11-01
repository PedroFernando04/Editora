from criar_conexao_editora import conexao

def verificar_email(email):
    conn = conexao()
    try:
        cursor = conn.cursor()
        query = "SELECT email_cliente FROM clientes WHERE email_cliente = %s"
        cursor.execute(query, (email,))
        conn.commit()
        row = cursor.fetchall()
        print("email verificado!")
        if row:
            print('E-mail já cadastrado!')
            email = input("Por favor, insira outro e-mail: ")
            verificar_email(email)
        else:
            print("E-mail válido!")
            return email
    except Exception as e:
        print(f"ERRO EMAIL: {e}")
    finally:
        cursor.close()
        conn.close()
