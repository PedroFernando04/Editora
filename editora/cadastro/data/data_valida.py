import os

def validacao_data(dia, mes, num, tipo, ano_atual):
    while True:
        match tipo:
                case 'dia':
                    if num < 1 or num > 31:
                        os.system('cls' or 'clear')
                        print("Valor inválido!")
                        print(f"O {tipo} deve ser um número entre 1 e 31\n")
                        num = int(input("Dia: "))
                    else:
                        return num
                case 'mes':
                    if num < 1 or num > 12:
                        os.system('cls' or 'clear')
                        print("Valor inválido!")
                        print(f"O {tipo} deve ser um número entre 1 e 12\n")
                        print(f"Dia: {dia}")
                        num = int(input("Mês: "))
                    else:
                        return num
                case _:
                    if num > ano_atual or num < 0:
                        os.system('cls' or 'clear')
                        print("Valor inválido!")
                        print(f"O {tipo} deve ser um número entre 1 e {ano_atual}\n")
                        print(f"Dia: {dia}")
                        print(f"Mês: {mes}")
                        num = int(input("Ano: "))
                    else:
                        return num
    
#DEF's com try except
def try_dia():
    while True:
        try:
            dia = int(input("Dia: "))
            dia_valido = validacao_data(0, 0, dia, 'dia', 2024)
            os.system('cls' or 'clear')
            return str(dia_valido)
        except Exception as e:
            os.system('cls' or 'clear')
            print("Formato inválido!")
            print("Informe dia válido!\n")
def try_mes(dia):
    while True:
        try:
            print(f"Dia: {dia}")
            mes = int(input("Mês: "))
            if dia > 29 and mes == 2:
                raise ValueError ('erro_fevereiro')
            mes_valido = validacao_data(dia, 0, mes, 'mes', 2024)
            os.system('cls' or 'clear')
            return str(mes_valido)
        except Exception as e:
            os.system('cls' or 'clear')
            print("Formato inválido!")
            print("Informe um mês válido!\n")
        except 'erro_fevereiro':
            os.system('cls' or 'clear')
            print("Formato inválido!")
            print(f"Data: {dia}/{mes} Não existe!\n")
            print("Informe um mês válido!\n")

        
def try_ano(dia, mes):
    while True:
        try:
            print(f"Dia: {dia}")
            print(f"Mês: {mes}")
            ano = int(input("Ano: "))
            ano_valido = validacao_data(dia, mes, ano, 'ano', 2024)
            os.system('cls' or 'clear')
            return str(ano_valido)
        except Exception as e:
            os.system('cls' or 'clear')
            print("Formato inválido!")
            print("Informe um ano válido!\n")


def data_valida():
    print("Data de Nascimento: ")

    dia_valido = try_dia()
    if len(dia_valido) < 2:
        dia_valido = f'0{dia_valido}' 

    mes_valido = try_mes(int(dia_valido))
    if len(mes_valido) < 2:
        mes_valido = f'0{mes_valido}' 

    ano_valido = try_ano(dia_valido, mes_valido)

    os.system('cls' or 'clear')
    data = f"{ano_valido}{mes_valido}{dia_valido}"

    print(f"Data de nascimento: {dia_valido}/{mes_valido}/{ano_valido}")
    return data
                
