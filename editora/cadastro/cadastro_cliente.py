from editora.cadastro.email.verificar_email import verificar_email
from editora.cadastro.email.email_valido import email_valido
from editora.cadastro.senha.senha_valida import senha_valida, mostrar_senha
from editora.cadastro.genero.genero_valido import genero_valido
from editora.cadastro.pais.verificar_pais import verificar_pais
from editora.cadastro.data.data_valida import data_valida
from editora.inserts.insert_editora import inserir_cliente
import os

def delay():
    input('\nAperte \'[Enter]\' para prosseguir')
    os.system('cls' or 'clear')

def cadastrar_cliente(conn):
    print("Vamos realizar o seu cadastro!")
    print("Por favor, preencha as informações solicitadas:\n")
    
    nome = input("Nome: ")
    delay()
    
    email = verificar_email(email_valido(), conn)
    delay()
    print(f"Nome: {nome}\nE-mail: {email}")
    delay()
    
    senha = senha_valida()
    delay()
    print(f"Nome: {nome}\nE-mail: {email}\nSenha:", end = " ")
    mostrar_senha(senha)
    delay()

    genero = genero_valido()
    delay()

    pais = verificar_pais(input("País: "), conn)
    delay()
    
    print("Data de Nascimento: ")
    data = data_valida()
    delay()
    
    inserir_cliente(conn, nome, email, senha, genero, pais, data)

    return nome, email, senha, genero, pais, data
