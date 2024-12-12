from editora.defs.defs_basicas import *

def verificar_pais(pais, conn):
    while True:
        try:
            cursor = conn.cursor()
            query = "SELECT id_pais FROM editora.paises WHERE nome_pais = %s"
            cursor.execute(query, (pais,))
            conn.commit()
            row = cursor.fetchone()
            clear()
            if row:
                print(f"País: {pais}")
                print('País cadastrado!')
                return row
            else:
                print(f"País: {pais}")
                print("País desconhecido!\n")
                pais = input("Insira um novo país: ")
        except Exception as e:
            print(f"ERRO PAIS: {e}")
        finally:
            cursor.close()
