import random

usuarios = [
    { 
        "nome": "administrador",
        "user": 123,
        "idade": 20,
        "senha": "123",
        "mensalidade": True, 
        "salario": 2000,
        "plano social": 0, 
        "plano sócio-torcedor": 6, 
        "forma de pagamento": 0 
    }
]

valor_ingresso = 100.00

def verificar_mensalidade():
    while True:
        try:
            mensalidade = int(input('''Qual o estado da sua mensalidade? 
    
1- Ativa 
2- Não ativa
: '''))
            if mensalidade == 1:    # Ativa
                return True
            elif mensalidade == 2:  # Não ativa
                print("Você não pode efetivar sua compra devido ao estado atual de sua mensalidade. \nTente novamente outro dia.")
                return False
            else:
                print('Opção inválida. Escolha 1 ou 2.')
        except ValueError:
            print('Você deve escolher uma das opções numéricas.')

def verificar_salario(salario):
    if (salario <= 800):
        desconto_percentual = valor_ingresso * 100 / 100
        valor_atual = valor_ingresso - desconto_percentual
        print(f"Você tem direito à 100% de desconto no seu ingresso devido ao plano social, o novo valor é {valor_atual} reais")
        return 1
    elif (salario <= 1200): 
        desconto_percentual = valor_ingresso * 75 / 100
        valor_atual = valor_ingresso - desconto_percentual
        print(f"Você tem direito à 75% de desconto no seu ingresso devido ao plano social, o novo valor é {valor_atual} reais")
        return 2
    elif (salario <= 1600):
        desconto_percentual = valor_ingresso * 25 / 100
        valor_atual = valor_ingresso - desconto_percentual
        print(f"Você tem direito à 25% de desconto no seu ingresso devido ao plano social, o novo valor é {valor_atual} reais")
        return 3
    else:
        print("Você não entra na categoria plano social.")
        return 0

def verificar_plano_socio_torcedor():
    while True:
        try:
            plano_socio_torcedor = int(input('''Qual plano sócio-torcedor você faz parte?
1 - Bronze
2 - Prata 
3 - Ouro
: '''))

            if plano_socio_torcedor == 1:
                desconto_percentual = valor_ingresso * 25 / 100
                valor_atual = valor_ingresso - desconto_percentual
                print(f'''Você tem acesso ao benefício de 25% de desconto em produtos oficiais.
O novo valor do seu ingresso é de R${valor_atual}''')
                return 4
            elif plano_socio_torcedor == 2:
                desconto_percentual = valor_ingresso * 50 / 100
                valor_atual = valor_ingresso - desconto_percentual
                print(f'''Você tem acesso ao benefício de 50% de desconto em produtos oficiais.
O novo valor do seu ingresso é de R${valor_atual}''')
                return 5
            elif plano_socio_torcedor == 3:
                desconto_percentual = valor_ingresso * 75 / 100
                valor_atual = valor_ingresso - desconto_percentual
                print(f'''Você tem acesso ao benefício de 75% de desconto em produtos oficiais.
O novo valor do seu ingresso é de R${valor_atual}''')
                return 6
            else:
                print("Opção inválida. Por favor, responda com '1', '2' or '3'.")
        except ValueError:    
            print("Por favor, insira um número válido.")

def forma_pagamento():
    try:
        forma = int(input("""Qual forma de pagamento você prefere?
            1 - Cartão de crédito
            2 - Cartão de débito
            3 - Pix
            : """))
    except ValueError:
        print("Opção de pagamento inválida.")
        return False
    
    if forma == 1:
        print("Você escolheu pagar com cartão de crédito.")
        numero_cartao = input("Digite o número do seu cartão de crédito (16 dígitos): ")
        if not numero_cartao.isdigit() or len(numero_cartao) != 16:
            print("Número de cartão inválido. Deve conter 16 dígitos numéricos.")
            return False
        primeiro_digito = numero_cartao[0]
        if primeiro_digito == "4":
            bandeira = "VISA"
        elif primeiro_digito == "5":
            bandeira = "MasterCard"
        elif primeiro_digito == "3":
            bandeira = "AmericanExpress"
        else:
            bandeira = "Bandeira desconhecida"
        print(f"Cartão {bandeira} - {numero_cartao[:4]} cadastrado com sucesso!")
        print("Compra finalizada com sucesso!")
        return True
    elif forma == 2:
        print("Você escolheu pagar com cartão de débito.")
        numero_cartao = input("Digite o número do seu cartão de débito (16 dígitos): ")
        if not numero_cartao.isdigit() or len(numero_cartao) != 16:
            print("Número de cartão inválido. Deve conter 16 dígitos numéricos.")
            return False
        primeiro_digito = numero_cartao[0]
        if primeiro_digito == "4":
            bandeira = "VISA"
        elif primeiro_digito == "5":
            bandeira = "MasterCard"
        elif primeiro_digito == "3":
            bandeira = "AmericanExpress"
        else:
            bandeira = "Bandeira desconhecida"
        print(f"Cartão {bandeira} - {numero_cartao[:4]} cadastrado com sucesso!")
        print("Compra finalizada com sucesso!")
        return True
    elif forma == 3:
        print("Você escolheu pagar com pix. Por favor, escaneie o código QR para finalizar a compra.")
        chave_pix = input("Digite a chave pix:")
        if chave_pix.strip() == "":
            print("Chave Pix inválida. Por favor, tente novamente.")
            return False
        print("Compra finalizada com sucesso!")
        return True
    else:
        print("Opção de pagamento inválida.")
        return False

def sair():
    print("Obrigado por utilizar nosso sistema. Até a próxima!")
    exit()

def menu():
    print("\n--- Menu de opções ---")
    print("1 - CADASTRO")
    print("2 - LOGIN E COMPRA")
    print("3 - SAIR")
    try:
        opcao = int(input("Selecione a opção de sua escolha: "))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            indice_usuario = login()
            if indice_usuario != -1:
                compra(indice_usuario)
        elif opcao == 3:
            sair() 
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Digite um número válido do menu.")

def cadastrar():
    while True:
        existe = False
        try:
            user = int(input("Digite seu CPF, que será seu usuário: "))
        except ValueError:
            print('Tente novamente. CPF inválido.')
            continue
            
        for usuario in usuarios:
            if usuario["user"] == user:
                print('Este usuário já existe')
                existe = True
                break
        if not existe:
            break

    try:
        nome = input("Digite seu nome completo: ").lower() 
        senha = input("Digite sua senha: ")
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print('Tente novamente. Dados inválidos.')
        return False

    if idade < 18:                                      
        print('Você deve ser maior de 18 anos para fazer uma compra.')
        return False
    elif idade <= 0:
        print('Idade inválida.')
        return False

    try:
        salario = float(input("Digite seu salário atual: "))
    except ValueError:
        print('Tente novamente. Salário inválido.')
        return False

    plano_social = verificar_salario(salario)
    plano_socio_torcedor = 0
    mensalidade_usuario = False

    if plano_social == 0:
        print("Você não tem direito ao plano social, mas pode aproveitar os benefícios do plano sócio-torcedor.")
        plano_socio_torcedor = verificar_plano_socio_torcedor()
        mensalidade_usuario = verificar_mensalidade()
                 
    usuario = {
        "nome": nome,
        "user": user,
        "idade": idade,
        "senha": senha,
        "mensalidade": mensalidade_usuario, 
        "salario": salario,
        "plano social": plano_social, 
        "plano sócio-torcedor" : plano_socio_torcedor, 
        "forma de pagamento": 0 
    }
    
    usuarios.append(usuario)
    print("Cadastro realizado com sucesso!")
    return True

def plano():
    try:
        A = int(input("""Você participa do plano social??
1- sim  
2- não: """))
    except ValueError:
        print("Opção inválida.")
        return

    if A == 1:
        print("O valor do seu ingresso depende do seu salário cadastrado.")
        forma_pagamento() 
    elif A == 2:
        try:
            B = int(input("""Ok! Gostaria de comprar seu ingresso pelo valor integral ou aproveitar os benefícios do plano sócio-torcedor?
1- Quero comprar pelo valor integral
2- Quero aproveitar os benefícios do plano sócio-torcedor
: """))
            if B == 1:
                print("Ótimo! Você pode efetivar sua compra pelo valor integral, o valor do seu ingresso é de 100,00 reais.")
                forma_pagamento()
            elif B == 2:
                plano_usuario = verificar_plano_socio_torcedor()
                mensalidade_usuario = verificar_mensalidade()   
                if plano_usuario == 4 and mensalidade_usuario == True:
                    print("Ótimo! Você pode efetivar sua compra, o valor do seu ingresso é de 75,00 reais.")
                    forma_pagamento()
                elif plano_usuario == 5 and mensalidade_usuario == True:
                    print("Ótimo! Você pode efetivar sua compra, o valor do seu ingresso é de 50,00 reais.")
                    forma_pagamento()
                elif plano_usuario == 6 and mensalidade_usuario == True:
                    print("Ótimo! Você pode efetivar sua compra, o valor do seu ingresso é de 25,00 reais.")
                    forma_pagamento()
                else:
                    print("Compra não autorizada (mensalidade inativa ou plano inválido).")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida.")

def compra(ind):
    print(f"\nBem-vindo {usuarios[ind]['nome']}! Vamos finalizar sua compra.")
    plano_social = usuarios[ind]['plano social']
    plano_torcedor = usuarios[ind]['plano sócio-torcedor']
    mensalidade_usuario = usuarios[ind]['mensalidade']
    
    # 1º Caso: Tem direito ao plano social
    if plano_social == 1:
        print("O valor do seu ingresso é de R$0,00 (100% de desconto pelo Plano Social).")
        print("Compra finalizada automaticamente!")
        return
    elif plano_social == 2:
        print("O valor do seu ingresso é de R$25,00 (75% de desconto pelo Plano Social).")
        forma_pagamento()
    elif plano_social == 3:
        print("O valor do seu ingresso é de R$75,00 (25% de desconto pelo Plano Social).")
        forma_pagamento()
        
    # 2º Caso: Depende do plano Sócio-Torcedor (precisa estar com a mensalidade ativa)
    elif plano_torcedor == 4 and mensalidade_usuario == True:
        print("O valor do seu ingresso é de 75,00 reais (Desconto Sócio-Torcedor Bronze).")
        forma_pagamento()
    elif plano_torcedor == 5 and mensalidade_usuario == True:
        print("O valor do seu ingresso é de 50,00 reais (Desconto Sócio-Torcedor Prata).")
        forma_pagamento()
    elif plano_torcedor == 6 and mensalidade_usuario == True:
        print("O valor do seu ingresso é de 25,00 reais (Desconto Sócio-Torcedor Ouro).")
        forma_pagamento()
    else:
        if plano_torcedor != 0 and mensalidade_usuario == False:
            print("Sua mensalidade de sócio-torcedor está atrasada! O valor cobrado será o integral.")
        print("O valor do seu ingresso é de 100,00 reais.")
        forma_pagamento()

def login():
    try:
        user = int(input("Digite seu CPF: "))
    except ValueError:
        print("CPF deve ser numérico.")
        return -1
        
    senha = input("Digite sua senha: ")
    
    indice = 0
    for usuario in usuarios:
        if usuario["user"] == user and usuario["senha"] == senha:
            print("Login bem-sucedido!") 
            return indice
        indice += 1
              
    print("Usuário ou senha incorretos.")
    return -1

# Loop principal do programa para manter o menu rodando de forma limpa
while True:
    menu()
    input("\nPressione Enter para continuar...")  # Pausa para o usuário conseguir ler as mensagens na tela
