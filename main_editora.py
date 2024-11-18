from editora.inserts.insert_editora import inserir_autor, inserir_editora, inserir_genero, inserir_livro, inserir_cliente
from editora.cadastro.cadastro_cliente import cadastrar_cliente

nome_editora = 'Edicria'
print(f"Bem vido a {nome_editora}!")
print("Aqui registramos os seus livros para sua melhor visualização\n")
while True:
    print("Informe o que deseja fazer:\n")
    print("1 - Casdastro")
    print("2 - Login")
    print("3 - Sair\n")
    opc = int(input())

    if opc == 1:
        #função retorna toso os campos do cadastro
        cadastro_cliente = cadastrar_cliente()
    elif opc == 2:
        #função booleana
        login_cliente = logar_cliente()
