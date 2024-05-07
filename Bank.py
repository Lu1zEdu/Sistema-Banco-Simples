import os
from datetime import datetime
import time
import sys

# Cores ANSI
RESET = "\033[0m"
VERMELHO = "\033[31m"
AMARELO = "\033[33m"
VERDE = "\033[32m"


Usuarios = {
    "joao": {
        "nome": "João",
        "idade": 30,
        "numero_conta": "123456",
        "saldo": 1000.00,
        "cpf": "123.456.789-00",
    },
    "maria": {
        "nome": "Maria",
        "idade": 25,
        "numero_conta": "789012",
        "saldo": 1500.50,
        "cpf": "987.654.321-00",
    },
    "carlos": {
        "nome": "Carlos",
        "idade": 35,
        "numero_conta": "345678",
        "saldo": 2000.75,
        "cpf": "543.210.987-00",
    },
    "Luiz": {
        "nome": "Luiz",
        "idade": 19,
        "numero_conta": "123456",
        "saldo": 20000000000,
        "cpf": "528.392.668-06",
    },
}


def menu_principal():
    """
    Menu Principal
    """
    print("1. Criar uma Nova Conta")
    print("2. Logar uma conta existente")
    print("3. Sair")
    escolha_menu_principal()


def escolha_menu_principal():
    """
    Função escolher a opção do menu
    """
    try:
        opcao = int(input("Escolha uma opção: \n"))
        if opcao == 1:
            criar_conta()
        elif opcao == 2:
            logar_conta()
        elif opcao == 3:
            Sair()
        else:
            print(VERMELHO + "Opção Invalida!" + RESET)
            input(AMARELO + "Precione ENTER \n" + RESET)
            main()
    except:
        print(VERMELHO + "Opção Invalida!" + RESET)
        input(AMARELO + "Precione ENTER \n" + RESET)
        main()


def Sair():
    """
    Função para Sair
    """
    print("sAIR")


def Limpar():
    os.system("cls")


def criar_conta():
    """
    Função para Criar Nova Conta
    """
    Limpar()
    nome = input("Nome: \n")
    if validar_nome(nome):
        Usuarios["nome"] = nome
        data_nascimento = input(
            f"{nome} , digite a data de nascimento (no formato DD/MM/AAAA): \n"
        )
        if validar_data_nascimento(data_nascimento):
            Usuarios["data_nascimento"] = data_nascimento
            try:
                idade = int(input(f"{nome} qual a sua Idade : \n"))
                if idade < 0:
                    raise ValueError("A idade não pode ser negativa.")
                elif idade > 120:
                    raise ValueError(
                        f"A idade não pode ser maior que 120 anos ou {idade}"
                    )
                else:
                    cpf = input(f"{nome} qual o seu CPF (somente números) : \n")
                    if validar_cpf(cpf):
                        if cpf not in Usuarios.values():
                            Usuarios["cpf"] = cpf
                            escolha = input(
                                f"Deseja continuar {nome}? [Sim] / [Nao] :  \n"
                            )
                            if (
                                escolha == "Sim"
                                or escolha == "sim"
                                or escolha == "S"
                                or escolha == "s"
                            ):
                                senha = input(
                                    f"{nome} qual a sua senha deseja colocar contendo 4 numero : \n"
                                )
                                if validar_senha_numerica(senha):
                                    Usuarios["senha"] = senha
                                    print("Conta criada com sucesso!")
                                    input(AMARELO + "Precione ENTER \n" + RESET)
                                    entrar(segundos=20)
                                else:
                                    print(
                                        VERMELHO
                                        + f"{nome} a senha [ {senha} ] não é válida. Certifique-se de inserir exatamente 4 dígitos numéricos."
                                        + RESET
                                    )
                                    input(AMARELO + "Precione ENTER \n" + RESET)
                                    main()

                            else:
                                print(
                                    AMARELO
                                    + f"Ok {nome} , irei te retorna para o menu"
                                    + RESET
                                )
                                input(AMARELO + "Precione ENTER \n" + RESET)
                                main()

                    else:
                        print(VERMELHO + f"{nome} CPF [ {cpf} ] não é válido." + RESET)
                        input(AMARELO + "Precione ENTER" + RESET)
                        main()

            except ValueError:
                print(VERMELHO + f"{nome} a idade [ {idade} ] não é válida." + RESET)
                input(AMARELO + "Precione ENTER\n" + RESET)
                main()
        else:
            print(
                VERMELHO
                + f"{nome}a data de nascimento [ {data_nascimento} ] não é válida."
                + RESET
            )
            input(AMARELO + "Precione ENTER\n" + RESET)
            main()
    else:
        print(VERMELHO + f"Nome [ {nome} ] não é válido." + RESET)
        input(AMARELO + "Precione ENTER\n" + RESET)
        main()


def validar_nome(nome):
    """
    Função para validar o nome do Usuario
    """
    # Verificar se o nome não está vazio
    if not nome:
        return False

    # Verificar se o nome contém apenas letras
    if not nome.isalpha():
        return False

    return True


def validar_data_nascimento(data):
    """
    Função para validar a data de nascimento do Usuario
    """
    try:
        # Tentar converter a string para um objeto datetime
        data_formatada = datetime.strptime(data, "%d/%m/%Y")

        # Verificar se a data está no passado (ou no presente)
        hoje = datetime.now()
        if data_formatada > hoje:
            return False

        return True

    except ValueError:
        # Se ocorrer um erro ao converter, a data não é válida
        return False


def validar_cpf(cpf):
    """
    Função para validar CPF do Usuario
    """
    # Remover caracteres não numéricos do CPF
    cpf = "".join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcular os dígitos verificadores
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto1 = soma1 % 11
    dv1 = 0 if resto1 < 2 else 11 - resto1

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto2 = soma2 % 11
    dv2 = 0 if resto2 < 2 else 11 - resto2

    # Verificar se os dígitos verificadores estão corretos
    if int(cpf[9]) != dv1 or int(cpf[10]) != dv2:
        return False

    return True


def validar_senha_numerica(senha):
    """
    Função para validar a senha numerida do Usuario
    """
    # Verificar se a senha possui exatamente 4 caracteres
    if len(senha) != 4:
        return False

    # Verificar se a senha contém apenas dígitos
    if not senha.isdigit():
        return False

    return True


def opcao_invalida():
    """
    Função para validar CPF do Usuario
    """
    Limpar()
    print("Opção Invalida!")
    input(AMARELO + "Precione ENTER\n" + RESET)
    main()


def logar_conta():
    """
    Função para validar CPF do Usuario
    """
    Limpar()
    nome = input("Qual o seu nome :\n")
    if verificar_nome(Usuarios, nome):
        senha = input("Qual a sua senha : \n")
        if verificar_senha(senha, Usuarios):
            NumeroDaConta = input("Qual o seu Numero da Conta :\n")
            if verificar_Numero_Da_Conta(Usuarios, NumeroDaConta):
                print("Login com sucesso !!!")
                input(AMARELO + "Precione ENTER \n" + RESET)
                entrar(segundos=20)
            else:
                print(
                    VERMELHO
                    + f"{nome} , colocou um [ {NumeroDaConta} ] invalido"
                    + RESET
                )
                input(AMARELO + "Precione ENTER\n" + RESET)
                erro_login_conta(segundos=20)
        else:
            print(VERMELHO + f"{nome} , colocou uma [ {senha} ] invalida" + RESET)
            input(AMARELO + "Precione ENTER\n" + RESET)
            erro_login_conta(segundos=20)
    else:
        print(VERMELHO + f"Nome de usuario [ {nome} ] inexistente" + RESET)
        input(AMARELO + "Precione ENTER\n" + RESET)
        erro_login_conta(segundos=20)


def verificar_nome(dicionario, nome):
    if nome in dicionario:
        print("Nome:", nome)
        print("Outras informações associadas:")
        for chave, valor in dicionario[nome].items():
            print(f"{chave}: {valor}")
    else:
        print(AMARELO + "Nome não encontrado." + RESET)


def verificar_senha(dicionario, senha):
    for nome, info in dicionario.items():
        if "senha" in info and info["senha"] == senha:
            print("Senha encontrada para o usuário:", nome)
            print("Outras informações associadas:")
            for chave, valor in info.items():
                if chave != "senha":  # Evita imprimir a senha
                    print(f"{chave}: {valor}")
            return
    print(AMARELO + "Senha incorreta." + RESET)


def verificar_Numero_Da_Conta(dicionario, NumeroDaConta):
    """
    Função para validar o Numero da Conta dp Usuario
    """
    for nome, info in dicionario.items():
        if "numero_conta" in info and info["numero_conta"] == NumeroDaConta:
            print("Número de conta encontrado para o usuário:", nome)
            print("Outras informações associadas:")
            for chave, valor in info.items():
                if chave != "numero_conta":  # Evita imprimir o número da conta
                    print(f"{chave}: {valor}")
            return
    print(AMARELO + "Número de conta não encontrado." + RESET)


def erro_login_conta(segundos):
    """
    Função de erro
    """
    print("erro login conta")
    input("Pressione Enter para voltar")
    for i in range(segundos, 0, -1):
        sys.stdout.write(VERDE + "\rTempo restante: {:2d} segundos".format(i) + RESET)
        sys.stdout.flush()
        time.sleep(1)
    print("\nTempo esgotado!")
    input(AMARELO + "Precione ENTER \n" + RESET)
    main()


def entrar(segundos):
    """
    Função antes de entrar
    """
    os.system("cls")
    print("ENTRANDO")
    for i in range(segundos, 0, -1):
        sys.stdout.write(VERDE + "\rTempo restante: {:2d} segundos".format(i) + RESET)
        sys.stdout.flush()
        time.sleep(1)
    print("\nTempo esgotado!")
    input(AMARELO + "Precione ENTER \n" + RESET)
    menu_da_conta_do_banco()


def menu_da_conta_do_banco():
    """
    Menu principal do Banco
    """
    print("")


def main():
    """
    Função da main
    """
    os.system("cls")
    menu_principal()
    escolha_menu_principal()


if __name__ == "__main__":
    main()
