import os

def email_valido():
    while True:
        email = input("E-mail: ")
        if '@' in email and '.' in email:
            print("E-mail válido!")
            return email
            
        else:
            os.system('cls' or 'clear')
            print("E-mail inválido!")
            print("Um e-mail válido deve conter um \'@\' e um \'.\'")
            print("Tente novamente\n")

#print(email_valido())