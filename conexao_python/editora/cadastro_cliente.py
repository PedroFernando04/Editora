from insert_editora import inserir_cliente
from verificar_email import verificar_email

def cadastrar_cliente():
    print("Vamos realizar o seu cadastro!")
    print("Por favor, preencha as informações solicitadas:\n")
    nome = input("Nome: ")
    email = input("E-mail: ")
    verificar_email(email)
    

    #inserir_cliente(nome, email, senha, genero, pais, data)
