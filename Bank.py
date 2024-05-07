import os

Usuarios = {}


def menu_principal():
    print("1. Criar uma Nova Conta")
    print("2. Logar uma conta existente")
    print("3. Sair")
    escolha_menu_principal()


def escolha_menu_principal():
    opcao = int(input("Escolha uma opção: \n"))
    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        logar_conta()
    elif opcao == 0:
        Sair()
    else:
        print("Opção Invalida!")
        escolha_menu_principal()


def Sair():
    pass


def criar_conta():
    nome = input("Nome: \n")
    Usuarios["nome"] = nome
    Data_Nasc = int(input(f"{nome} qual a sua Data de Nascimento : \n"))
    Usuarios["Data_Nasc"] = Data_Nasc
    cpf = int(input(f"{nome} qual o seu CPF: \n"))
    Usuarios["cpf"] = cpf
    if cpf in Usuarios.values():
        print("CPF ja existente!")
        criar_conta()
    else:
        escolha = input(f"Deseja continuar {nome}? [Sim] / [Nao] :  \n")
        try:
            if escolha == "Sim" or escolha == "sim" or escolha == "S" or escolha == "s":
                senha = int(input(f"{nome} qual a sua senha {cpf}: \n"))
                try:
                    if senha in Usuarios.values():
                        print("Senha ja existente!")
                        criar_conta()
                    else:
                        Usuarios["senha"] = senha
                        print("Conta criada com sucesso!")
                        input("Pressione Enter para continuar")
                        main()
                except:
                    opcao_invalida()
            elif (
                escolha == "Nao" or escolha == "nao" or escolha == "N" or escolha == "n"
            ):
                main()
            else:
                opcao_invalida()

        except:
            opcao_invalida()


def opcao_invalida():
    os.system("cls")
    print("Opção Invalida!")
    input("Pressione Enter para continuar")
    main()


def logar_conta():
    pass


def main():
    os.system("cls")
    menu_principal()


if __name__ == "__main__":
    main()
