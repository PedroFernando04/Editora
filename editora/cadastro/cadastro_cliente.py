from editora.cadastro.email.verificar_email import verificar_email
from editora.cadastro.email.email_valido import email_valido
from editora.cadastro.senha.senha_valida import senha_valida, mostrar_senha
from editora.cadastro.genero.genero_valido import genero_valido
from editora.cadastro.pais.verificar_pais import verificar_pais
from editora.cadastro.data.data_valida import data_valida
import os

def delay():
    input('\nAperte \'enter\' para prosseguir')
    os.system('cls' or 'clear')

def cadastrar_cliente():
    print("Vamos realizar o seu cadastro!")
    print("Por favor, preencha as informações solicitadas:\n")
    
    nome = input("Nome: ")
    delay()
    
    email = verificar_email(email_valido())
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

    pais = verificar_pais(input("País: "))
    delay()

    data = data_valida()
    delay()
    
    #inserir_cliente(nome, email, senha, genero, pais, data)

    return nome, email, senha, genero, pais, data


