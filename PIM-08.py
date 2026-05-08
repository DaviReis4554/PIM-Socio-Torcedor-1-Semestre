usuarios = []

valor_ingresso = 100.00
# coloquei cadastro e login la pra baixo pra se precisar chamar a verif de idade, mas na vdd ja fiz ela no propio cadastro



def verificar_mensalidade():#perguntar o salario antes de perguntar da mensalidade.
    # se a pessoa fizer parte do beneficio, e tiver 100% de desconto, nao precisa pagar mensalidade?
    while True:
     try:
      mensalidade = int(input('''Qual o estado da sua mensalidade? 
1- Ativa 
2- Não ativa 
3- Em atraso):'''))
     except VallueError:
      print('Você deve escolher uma das opções.')
      break
    if mensalidade == "ativa":
        return True
    elif mensalidade == "em atraso":
        print("Você precisa estar com sua mensalidade atualizada para efetuar sua compra. \n Tente novamente mais tarde.")
        return False
    else:
        print("Você não pode efetivar sua compra devido ao estado atual de sua mensalidade. \n Tente novamente outro dia.")
        return False



def verificar_salario(salario):# aqui fizemos um cálculo baseado no valor do salário mínimo atual
    if (salario <= 800):
       desconto_percentual = valor_ingresso*100/100
       valor_atual = valor_ingresso - desconto_percentual
       print(f"Foi aplicado um desconto de 100% no seu ingresso, o novo valor é {valor_atual} reais")
    elif (salario <= 1.200 ):
         desconto_percentual = valor_ingresso*75/100
         valor_atual = valor_ingresso - desconto_percentual
         print(f"Foi aplicado um desconto de 75% no seu ingresso, o novo valor é {valor_atual} reais")
    elif (salario <= 1.600):
         desconto_percentual = valor_ingresso*25/100
         valor_atual = valor_ingresso - desconto_percentual
         print(f"Foi aplicado um desconto de 25% no seu ingresso, o novo valor é {valor_atual} reais")
    elif (salario <= 2.000):
         desconto_percentual = valor_ingresso*25/100
         valor_atual = valor_ingresso - desconto_percentual
    else:
        print("Você não entra na categoria plano social. Realize sua compra no modo padrão.")


def verificar_plano_social(): # colocar primeiro input de salario, depois ja dizer se a
    # pessoa se qualifica ou não e mostrar o desconto para ela. em seguida ja passar pra etapa de mensalidade
    plano_social = int(input('''Você tem direito ao plano social? 
1 - Sim 
2 - Não):'''))
    
    if plano_social == "1":
        return True
    elif plano_social == "2":
        compra = int(input('''Você não faz parte do plano social, portanto não tem acesso a este benefício. 
        Gostaria de comprar comprar o ingresso mesmo assim?
1 - Sim
2 - Não'''))
        #if compra == 1:
         # ir para compras

        return False
    else:
        print("Resposta inválida. Por favor, responda com '1' ou '2'.")
        return False


def verificar_plano_socio_torcedor():
    plano_socio_torcedor = input('''Qual plano sócio-torcedor você faz parte?
1 - Bronze
2 - Prata 
3 - Ouro):''').lower()

    if plano_socio_torcedor == "1":
        print("Você tem acesso ao benefício de 25% de desconto em produtos oficiais do clube.")
        return True
    elif plano_socio_torcedor == "2":
        print("Você tem acesso ao benefício de 50% de desconto em produtos oficiais do clube.")
        return True
    elif plano_socio_torcedor == "3":
        print("Você tem acesso ao benefício de 75% de desconto em produtos oficiais do clube.")
        return True
    else:
        print("Plano sócio-torcedor inválido. Por favor, responda com 'bronze', 'prata' ou 'ouro'.")
        return False


def forma_pagamento():
    forma_pagamento = input("""Qual forma de pagamento você prefere?
1 - Cartão de crédito
2 - Cartão de débito
3 - Pix
: """).lower()
    
    if forma_pagamento == "1":
        print("Você escolheu pagar com cartão de crédito. Por favor, insira os dados do seu cartão para finalizar a compra.")
        return True
    elif forma_pagamento == "2":
        print("Você escolheu pagar com cartão de débito. Por favor, insira os dados do seu cartão para finalizar a compra.")
        return True
    elif forma_pagamento == "3":
        print("Você escolheu pagar com pix. Por favor, escaneie o código QR para finalizar a compra.")
        return True
    else:
        print("Forma de pagamento inválida. Por favor, responda com '1', '2o' ou '3'.")
        return False


def sair():
    print("Obrigado por utilizar nosso sistema. Até a próxima!")
    exit()


def menu():
    while True:
        print("Menu de opções:")
        print("1 - CADASTRO")
        print("2 - LOGIN E COMPRA ")
        print("3 - SAIR")
        opcao = int(input("Selecione a opção de sua escolha: "))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            login()
        elif opcao == 3:
            exit()
        else:
            print("Opção inválida. Tente novamente.")


def cadastrar():
    while True:
        try:
            nome = input("Digite seu nome completo: ").lower()
            user = int(input("Digite seu CPF, que será seu usuário: "))
            senha = input("Digite sua senha: ")
            idade = int(input("Digite sua idade: "))
            if idade < 18:                                    #Aqui eu modifiquei o idade <=18 para apenas =18, se deixasse como tava, a pessoa mesmo com 18 anos, não conseguia se cadastrar - DAVI
                print('Você deve ser maior de 18 anos para fazer uma compra.')
                break
            elif idade <= 0:
                print('Idade inválida.')
                break
            else:
                mensalidade = input('''Digite o estado da sua mensalidade
1 - ativa
2 - Não ativa 
3 - Em atraso):
''').lower()
                salario = float(input("Digite seu salário atual:"))
                plano_social = input("Digite se você participa do plano social:").lower()
                plano_socio_torcedor = input(f'''Digite qual plano sócio-torcedor você faz parte:
1 - Bronze
2 - Prata
3 - Ouro
4- Sou elegivel para o programa social: ''' ).lower()
                forma_pagamento = input("Digite qual forma de pagamento você prefere:").lower() #forma de pagamento em cadastro nao faz sentido pra mim, so na hora da compra
                usuario = {
                    "nome": nome,
                    "user": user,
                    "idade": idade,
                    "senha": senha,
                    "mensalidade": mensalidade,
                    "salario": salario,
                    "plano social": plano_social,
                    "plano sócio-torcedor": plano_socio_torcedor,
                    "forma de pagamento": forma_pagamento
                }

                usuarios.append(usuario)
                print("Cadastro realizado com sucesso!")
                menu()              #Aqui, faltava esse menu() no final do cadastro, para poder voltar para o menu, e acessar a tela de Login e compra - DAVI
        except:
            print('Tente novamete. Algo deu errado.')

def login():
    user = int(input("Digite seu CPF:"))
    senha = input("Digite sua senha:")
    for usuario in usuarios:
        if usuario["user"] == user and usuario["senha"] == senha:
            print("Login bem-sucedido!")
            return True
    print("Usuário ou senha incorretos.")
    return False


while True: #não era necessario fazer essa etapa, ela ja estava feita em menu()
    print(menu())
    # print("Menu de opções:")
    # print("1 - CADASTRO ")
    # print("2 - LOGIN E COMPRA")
    # print("3 - SAIR")
    # opção = int(input("Selecione a opção de sua escolha:"))
    # if opção == 1:
    #     cadastrar()
    # elif opção == 2:
    #     login()
    # elif opção == 3:
    #     sair()
    # else:
    #     print("Opção inválida. Tente novamente.")


#antes de finalizar a compra, o sistema irá verificar se o usuário tem direito a algum desconto baseado no salário, plano social e plano sócio-torcedor. O sistema também irá verificar se a mensalidade do usuário está ativa para que ele possa efetivar sua compra.
#observações: questão dos acentos gráficos, o sistema não aceita acentos, então as palavras devem ser digitadas sem acentos para que o sistema funcione corretamente. Exemplo: "sim" ao invés de "sím".
#fazer uma opção no menu para compra    
    
    