from insert_editora import inserir_cliente
from verificar_email import verificar_email

def cadastrar_cliente():
    print("Vamos realizar o seu cadastro!")
    print("Por favor, preencha as informações solicitadas:\n")
    nome = input("Nome: ")
    ler_email = input("E-mail: ")
    email = verificar_email(ler_email)
    

    #inserir_cliente(nome, email, senha, genero, pais, data)
