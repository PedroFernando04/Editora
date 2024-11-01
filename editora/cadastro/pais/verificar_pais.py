from criar_conexao_editora import conexao

def verificar_pais(pais):
    conn = conexao()
    try:
        cursor = conn.cursor()
        query = "SELECT nome_pais FROM paises WHERE nome_pais = %s"
        cursor.execute(query, (pais,))
        conn.commit()
        row = cursor.fetchall()
        print("país verificado!")
        if row:
            print('País presente no banco')
            return pais
        else:
            print("País desconhecido!")
            pais = input("Insira um novo país: ")
            verificar_pais(pais)
    except Exception as e:
        print(f"ERRO PAIS: {e}")
    finally:
        cursor.close()
        conn.close()
