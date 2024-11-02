from editora.conexao.criar_conexao_editora import conexao
import os

def verificar_pais(pais):
    while True:
        conn = conexao()
        try:
            cursor = conn.cursor()
            query = "SELECT nome_pais FROM paises WHERE nome_pais = %s"
            cursor.execute(query, (pais,))
            conn.commit()
            row = cursor.fetchall()
            if row:
                os.system('cls' or 'clear')
                print(f"País: {pais}")
                print('País cadastrado!')
                return pais
            else:
                os.system('cls' or 'clear')
                print(f"País: {pais}")
                print("País desconhecido!\n")
                pais = input("Insira um novo país: ")
        except Exception as e:
            print(f"ERRO PAIS: {e}")
        finally:
            cursor.close()
            conn.close()
