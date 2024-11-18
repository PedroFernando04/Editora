from editora.conexao.criar_conexao_editora import conexao
import os

def logar_cliente():
    email = input("Login: ")
    senha = input("Senha: ")

    conn = conexao()
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM editora.clientes WHERE email_cliente = '{email}' AND senha_cliente = '{senha}'"
        cursor.execute(query)
        conn.commit()
        row = cursor.fetchall()
    except Exception as e:
        print(f"ERRO: {e}")
    finally:
        cursor.close()
        conn.close()
    
    if row:
        return True
    else:
        return False

    
