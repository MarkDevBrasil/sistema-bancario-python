
# Função principal do banco
def menu_banco():
# Area de variaveis
 saldo = 0
 saque = None
 deposito = int
# Estruturas de repetição
 while True:
        loginB = int(input("""
========    Bem vindo Ao sistema do banco ! 🏦 ==============
[1] Ver saldo
[2] Sacar
[3] Depositar
[4] Sair do sistema
Escolha: """))
# Casos
        match loginB:
                case 1:
                    print(f"Seu saldo atual é de {saldo}")
                case 2:
                   saque = int(input("Digite o valor do saque: "))
                   print(f"Parabéns, você sacou R$ {saque}")
                   if saldo < saque:
                        print("Você não tem saldo o suficiente para sacar!")
                   else:
                       saldo -= saque
                       print(f"Parabéns, você sacou {saque}")
                case 3:
                    deposito = int(input("Digite o valor do deposito: "))
                    saldo += deposito
                    print(f"Parabéns, você depositou: {deposito} e seu saldo agora é de: {saldo}")
                case 4:
                    print("Saindo....")
                    break
                case _:
                    print("Opção invalida, tente novamente.")
pass
# Função tela de login
def login_tela():
    print("====================================="
          "          BRADESCO LOGIN   🏦💸     "
          "=====================================")
    # Variaveis
    usuario = ""
    senha = ""

    # While
    while True:
        login = int(input("""
    Bem vindo Ao banco Bradesco!

[1] Registro
[2] Login
[3] Sair
Escolha: """))
        # Escolha caso
        match login:
            # Casos
            case 1:
                usuario = input("Bem vindo ao registro, digite seu CPF (Apenas numeros): ")
                senha = input("Digite a senha desejada: ")
                print(f"Parabéns, CPF registrado com sucesso, bem vindo {usuario}!")

            case 2:
                print("======== SISTEMA DE LOGIN ==============")
                log = input("Digite seu CPF para login: ")
                senhaL = input("Digite a senha da sua conta: ")

                if log == usuario and senhaL == senha:
                    print("Login com sucesso")
                    menu_banco()
                else:
                    print("Usuário não encontrado ou senha incorreta.")
            case 3:
                print("Saindo...")
                break

            case _:
                print("Inválido, tente novamente.")
login_tela()



