from editora.conexao.criar_conexao_editora import conexao
from editora.cadastro.email.email_valido import email_valido
from editora.defs.defs_basicas import *


def verificar_email(email, conn):
    while True:
        try:
            cursor = conn.cursor()
            query = "SELECT email_cliente FROM editora.clientes WHERE email_cliente = %s"
            cursor.execute(query, (email,))
            conn.commit()
            row = cursor.fetchall()
            if row:
                clear()
                print('E-mail já cadastrado!')
                print("Por favor, insira outro e-mail ")
                email = email_valido()
            else:
                return email
        except Exception as e:
            print(f"ERRO EMAIL: {e}")
        finally:
            cursor.close()
            

