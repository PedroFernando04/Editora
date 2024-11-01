from criar_conexao_editora import conexao

def verificar_pais(pais):
    conn = conexao()
    while True:
        try:
            cursor = conn.cursor()
            query = "SELECT email_cliente FROM clientes WHERE email_cliente = %s"
            cursor.execute(query, (pais,))
            conn.commit()
            row = cursor.fetchall()
            print("email verificado!")
            if row:
                print('País presente no banco')
                return pais
            else:
                print("País desconhecido!")
                print("Tente novamente!")
        except Exception as e:
            print(f"ERRO PAIS: {e}")
        finally:
            cursor.close()
            conn.close()
    
