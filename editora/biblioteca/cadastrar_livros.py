#nome
#autor - select 
#editora - select
#data
#genero
#status - select
#ano
#nota
#resenha
#(id_cliente)

from editora.defs.defs_basicas import *
from editora.cadastro.data.data_valida import data_valida
import os

class cadastro_livro():
    def __init__():
        print("Vamos cadastrar um novo livro!")
        print("Por favor insira as informações requisistadas")

    def nome_livro(conn):
        while True:
            delay()
            nome_livro = input("Nomde do livro: ")

            cursor = conn.cursor()
            query = "SELECT nome_livro FROM editora.livros WHERE nome_livro = %s"
            cursor.execute(query, (nome_livro,))
            row = cursor.fetchone()

            if row:
                print("Livro já cadastrado!")
            else: 
                print("Nome cadastrado com sucesso!")
                delay()
                return nome_livro
    
    def autor_livro(conn):
        while True:

            print("Selecione o autor do livro:")

            cursor = conn.cursor()
            query = "SELECT id_autor, nome_autor FROM editora.autores"
            cursor.execute(query)
            row = cursor.fetchall()

            range_lista = []
            r = 0

            print("-"*100)
            for i in row:
                print(f"{i[0]} - {i[1]}")
                r += 1
                range_lista.append(str(r))
            print("-"*100)

            editora_livro = input("Informe o autor pelo seu respectivo número: ")

            if editora_livro in range_lista:
                delay()
                return editora_livro
            else:
                os.system('cls' or 'clear')
                print("Valor inválido!")
                print("Informe um número conforme a tabela\n")

    def editora_livro(conn):
        while True:

            print("Selecione a editora do livro:")

            cursor = conn.cursor()
            query = "SELECT id_editora, nome_editora FROM editora.editoras"
            cursor.execute(query)
            row = cursor.fetchall()

            range_lista = []
            r = 0

            print("-"*100)
            for i in row:
                print(f"{i[0]} - {i[1]}")
                r += 1
                range_lista.append(str(r))
            print("-"*100)

            editora_livro = input("Informe a editora pelo seu respectivo número: ")

            if editora_livro in range_lista:
                delay()
                return editora_livro
            else:
                os.system('cls' or 'clear')
                print("Valor inválido!")
                print("Informe um número conforme a tabela\n")
    
    def data_livro():
        return data_valida()

    def genero_livro(conn):
        while True:

            print("Selecione o genero do livro:")

            cursor = conn.cursor()
            query = "SELECT id_genero, nome_genero FROM editora.generos"
            cursor.execute(query)
            row = cursor.fetchall()

            range_lista = []
            r = 0

            print("-"*100)
            for i in row:
                print(f"{i[0]} - {i[1]}")
                r += 1
                range_lista.append(str(r))
            print("-"*100)

            genero_livro = input("Informe o genero pelo seu respectivo número: ")

            if genero_livro in range_lista:
                return genero_livro
            else:
                os.system('cls' or 'clear')
                print("Valor inválido!")
                print("Informe um número conforme a tabela\n")

    def status_livro(conn):
        while True:

            print("Selecione o status do livro:")

            cursor = conn.cursor()
            query = "SELECT id_status, nome_status FROM editora.status"
            cursor.execute(query)
            row = cursor.fetchall()

            range_lista = []
            r = 0

            print("-"*100)
            for i in row:
                print(f"{i[0]} - {i[1]}")
                r += 1
                range_lista.append(str(r))
            print("-"*100)

            status_livro = input("Informe o status pelo seu respectivo número: ")

            if status_livro in range_lista:
                return status_livro
            else:
                os.system('cls' or 'clear')
                print("Valor inválido!")
                print("Informe um número conforme a tabela\n")
    
    def ano_lido_livro(ano_atual = 2024):
        while True:
            try:
                ano_lido = int(input("Ano lido: "))
                if ano_lido < 0 or ano_lido > ano_atual:
                    raise Exception('Data inválida')
            except Exception:
                os.system('cls' or 'clear')
                print('Data inválida')
            else:
                return ano_lido
            
    def nota_livro():

        while True:
            try:
                nota = int(input('Informe a nota do livro(0 a 10): '))
                if nota < 0 or nota > 10:
                    raise Exception('Nota inválida')
            except Exception:
                os.system('cls' or 'clear')
                print('Nota inválida')
            else:
                delay()
                return nota

    def resenha_livro():
        resenha_livro = input("Resenha: ")
        return resenha_livro
