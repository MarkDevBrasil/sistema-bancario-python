import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


# Função principal do banco
def menu_banco():
# Variavel principal da função
    saldo = 0
# Escolha
    while True:
        limpar_tela()

        try:
            loginB = int(input("""
======== Bem-vindo ao sistema do banco! 🏦 ========

[1] Ver saldo
[2] Sacar
[3] Depositar
[4] Sair do sistema

Escolha: """))
# Exeções
        except ValueError:
            print("Digite apenas números.")
            pausar()
            continue
# Escolha caso
        match loginB:
            case 1:
                limpar_tela()
                print("======== SALDO ========")
                print(f"Seu saldo atual é de R$ {saldo}")
                pausar()

            case 2:
                limpar_tela()
                print("======== SAQUE ========")

                try:
                    saque = float(input("Digite o valor do saque: R$ "))
                except ValueError:
                    print("Valor inválido.")
                    pausar()
                    continue

                if saque <= 0:
                    print("O valor do saque precisa ser maior que zero.")
                elif saldo < saque:
                    print("Você não tem saldo suficiente para sacar!")
                else:
                    saldo -= saque
                    print(f"Saque de R$ {saque} realizado com sucesso!")
                    print(f"Seu saldo atual é de R$ {saldo}")

                pausar()

            case 3:
                limpar_tela()
                print("======== DEPÓSITO ========")

                try:
                    deposito = float(input("Digite o valor do depósito: R$ "))
                except ValueError:
                    print("Valor inválido.")
                    pausar()
                    continue

                if deposito <= 0:
                    print("O valor do depósito precisa ser maior que zero.")
                else:
                    saldo += deposito
                    print(f"Depósito de R$ {deposito} realizado com sucesso!")
                    print(f"Seu saldo atual é de R$ {saldo}")

                pausar()

            case 4:
                limpar_tela()
                print("Saindo do sistema bancário...")
                pausar()
                break

            case _:
                print("Opção inválida, tente novamente.")
                pausar()


# Função tela de login
def login_tela():
# Variaveis
    usuario = ""
    senha = ""
# Repetição
    while True:
        limpar_tela()

        print("""
=====================================
          BRADESCO LOGIN 🏦💸
=====================================
""")

        try:
            login = int(input("""
Bem-vindo ao banco Bradesco!

[1] Registro
[2] Login
[3] Sair

Escolha: """))
# Exeções
        except ValueError:
            print("Digite apenas números.")
            pausar()
            continue
# Escolha caso
        match login:
            case 1:
                limpar_tela()
                print("======== REGISTRO ========")

                usuario = input("Digite seu CPF apenas com números: ")
                senha = input("Digite a senha desejada: ")

                print(f"\nCPF registrado com sucesso!")
                print(f"Bem-vindo, {usuario}!")

                pausar()

            case 2:
                limpar_tela()
                print("======== SISTEMA DE LOGIN ========")

                log = input("Digite seu CPF para login: ")
                senhaL = input("Digite a senha da sua conta: ")

                if log == usuario and senhaL == senha:
                    print("\nLogin realizado com sucesso!")
                    pausar()
                    menu_banco()
                else:
                    print("\nUsuário não encontrado ou senha incorreta.")
                    pausar()

            case 3:
                limpar_tela()
                print("Saindo...")
                break

            case _:
                print("Opção inválida, tente novamente.")
                pausar()


login_tela()
