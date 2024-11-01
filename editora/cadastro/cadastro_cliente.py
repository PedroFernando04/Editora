from insert_editora import inserir_cliente
from verificar_email import verificar_email
from senha_valida import senha_valida
from email_valido import email_valido
from genero_valido import genero_valido
from verificar_pais import verificar_pais

def cadastrar_cliente():
    print("Vamos realizar o seu cadastro!")
    print("Por favor, preencha as informações solicitadas:\n")
    
    nome = input("Nome: ")
    
    email = verificar_email(email_valido())
    
    senha = senha_valida()

    genero = genero_valido()

    pais = verificar_pais(input("Nacionalidade: "))
    
    inserir_cliente(nome, email, senha, genero, pais, data)
