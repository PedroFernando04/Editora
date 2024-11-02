from editora.conexao.criar_conexao_editora import conexao
from editora.cadastro.email.email_valido import email_valido
import os


def verificar_email(email):
    while True:
        conn = conexao()
        try:
            cursor = conn.cursor()
            query = "SELECT email_cliente FROM clientes WHERE email_cliente = %s"
            cursor.execute(query, (email,))
            conn.commit()
            row = cursor.fetchall()
            if row:
                os.system('cls' or 'clear')
                print('E-mail já cadastrado!')
                print("Por favor, insira outro e-mail ")
                email = email_valido()
            else:
                return email
        except Exception as e:
            print(f"ERRO EMAIL: {e}")
        finally:
            cursor.close()
            conn.close()

