#fazer match case
from editora.inserts.insert_editora import *
from editora.defs.defs_basicas import *
from editora.cadastro.data.data_valida import data_valida
from editora.cadastro.genero.genero_valido import genero_valido
from editora.cadastro.pais.verificar_pais import verificar_pais
from editora.biblioteca.menus.menu_editora import menu_editora

def menu_mod(conn, id_cliente):
    while True:
        print("Informe o que deseja fazer:\n")
        print("1 - Cadastrar autor(a)")
        print("2 - Cadastrar editora")
        print("3 - Cadastrar genero")
        print("4 - Menu padrão")
        print("5 - Sair\n")
        opc = (input())
        clear()

        match(opc):
            case '1':
                nome = input("Nome do(a) autor(a): ")
                clear()

                print("Insira a data de nascimento do(a) autor(a):\n")
                data = data_valida()
                clear()

                genero = genero_valido()
                clear()

                pais = verificar_pais(input("País: "), conn)
                clear()

                inserir_autor(conn, nome, data, genero, pais)
                print("Autor cadastrado com sucesso!")
                delay()
           
            case '2':
                print("Insira o nome da nova editora\n")
                inserir_editora(conn, input("Editora: "))
                clear()
                print("Editora cadastrada com sucesso!")
                delay()

            case '3':  
                print("Insira o novo gênero\n")
                inserir_genero(conn, input("Gênero: "))
                clear()
                print("Gênero cadastrado com sucesso!")
                delay()
            
            case '4':
                menu_editora(conn, id_cliente)

            case '5':
                exit()

            case _:
                clear()
                print("Valor inválido!\n")
                
