import os

Usuarios = {
    "nome": "Luiz Edu",
    "senha": "123",
    "saldo": "1,000,000.00",
    "Data_Nasc": "15/09/2004",
}


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


def verificar_maioridade(idade):
    if idade >= 18:
        return True
    else:
        return False


def criar_conta():
    nome = input("Nome: \n")
    Usuarios["nome"] = nome
    Data_Nasc = int(input(f"{nome} qual a sua Data de Nascimento : \n"))
    idade = int(input(f"{nome} qual a sua Idade : \n"))
    if verificar_maioridade(idade):
        Usuarios["Data_Nasc"] = Data_Nasc
        cpf = int(input(f"{nome} qual o seu CPF: \n"))
        Usuarios["cpf"] = cpf
        if cpf in Usuarios.values():
            print("CPF ja existente!")
            criar_conta()
        else:
            escolha = input(f"Deseja continuar {nome}? [Sim] / [Nao] :  \n")
            if escolha == "Sim" or escolha == "sim" or escolha == "S" or escolha == "s":
                senha = int(input(f"{nome} qual a sua senha {cpf}: \n"))
                if senha in Usuarios.values():
                    print("Senha ja existente!")
                    criar_conta()
                else:
                    Usuarios["senha"] = senha
                    print("Conta criada com sucesso!")
                    input("Pressione Enter para continuar")
                    main()

            else:
                main()
    else:
        print("A pessoa é menor de idade. ")


def opcao_invalida():
    os.system("cls")
    print("Opção Invalida!")
    input("Pressione Enter para continuar")
    main()


def logar_conta():
    nome = str(input("Qual o seu nome :\n"))
    if nome in Usuarios.values():
        senha = int(input("Qual a sua senha : \n"))
        if senha in Usuarios.values():
            NumeroDaConta = int(input("Qual o seu Numero da Conta :\n"))
            if NumeroDaConta in Usuarios.values():
                entrar()
            else:
                print(f"{nome} , colocou um {NumeroDaConta} invalido")
                erro_login_conta()
        else:
            print(f"{nome} , colocou uma {senha} invalida")
            erro_login_conta()
    else:
        print("Nome de usuario inexistente")
        erro_login_conta()


def erro_login_conta():
    input("Pressione Enter para voltar")
    main()


def entrar():
    print("Login com sucesso !!!")
    input("Pressione Enter para continuar")
    menu_da_conta_do_banco()


def menu_da_conta_do_banco():
    print("")


def main():
    os.system("cls")
    menu_principal()


if __name__ == "__main__":
    main()
