import random
usuarios = []

valor_ingresso = 100.00
# coloquei cadastro e login la pra baixo pra se precisar chamar a verif de idade, mas na vdd ja fiz ela no propio cadastro - mi


def verificar_mensalidade():

     try:
         mensalidade = int(input('''Qual o estado da sua mensalidade? 
1- Ativa 
2- Não ativa 
3- Em atraso
: '''))
         if mensalidade == 1:    #Ativa
            return True
         elif mensalidade == 3:        #em atraso
            print("Você precisa estar com sua mensalidade atualizada para efetuar sua compra. \n Tente novamente mais tarde.")
            return False
         else:       #Não ativa
             print("Você não pode efetivar sua compra devido ao estado atual de sua mensalidade. \n Tente novamente outro dia.")
             return False

     except ValueError:
      print('Você deve escolher uma das opções.')

        

desconto_percentual = 0
def verificar_salario(salario):# aqui fizemos um cálculo baseado no valor do salário mínimo atual
    if (salario <= 800):
       desconto_percentual = valor_ingresso*100/100
       valor_atual = valor_ingresso - desconto_percentual
       print(f"Você tem direito à 100% de desconto no seu ingresso devido ao plano social, o novo valor é {valor_atual} reais")
    elif (salario <= 1200 ): 
         desconto_percentual = valor_ingresso*75/100
         valor_atual = valor_ingresso - desconto_percentual
         print(f"Você tem direito à 75% de desconto no seu ingresso devido ao plano social, o novo valor é {valor_atual} reais")
    elif (salario <= 1600):
         desconto_percentual = valor_ingresso*25/100
         valor_atual = valor_ingresso - desconto_percentual
         print(f"Você tem direito à 25% de desconto no seu ingresso devido ao plano social, o novo valor é {valor_atual} reais")
    elif (salario <= 2000):
         desconto_percentual = valor_ingresso*25/100
         valor_atual = valor_ingresso - desconto_percentual
    elif (salario > 2000):
        print("Você não entra na categoria plano social.")
        return False


def verificar_plano_social(): 
    plano_social = int(input('''Você tem direito ao plano social? 
1 - Sim 
2 - Não):'''))
    
    if plano_social == 1:
        return True
    elif plano_social == 2:
        compra = int(input('''Você não faz parte do plano social, portanto não tem acesso a este benefício. 
        Gostaria de comprar comprar o ingresso mesmo assim?
1 - Sim
2 - Não'''))
        if compra == 1:
         compra()
        return False
    else:
        print("Resposta inválida. Por favor, responda com '1' ou '2'.")
        return False


def verificar_plano_socio_torcedor():
 try:

    plano_socio_torcedor = int(input('''Qual plano sócio-torcedor você faz parte?
1 - Bronze
2 - Prata 
3 - Ouro
: '''))

    if plano_socio_torcedor == 1:
        desconto_percentual = valor_ingresso*25/100
        valor_atual = valor_ingresso - desconto_percentual
        print(f'''Você tem acesso ao benefício de 25% de desconto em produtos oficiais.
O novo valor do seu ingresso é de R${valor_atual}''')
        return True
    elif plano_socio_torcedor == 2:
        desconto_percentual = valor_ingresso*50/100
        valor_atual = valor_ingresso - desconto_percentual
        print(f'''Você tem acesso ao benefício de 50% de desconto em produtos oficiais.
O novo valor do seu ingresso é de R${valor_atual}''')
        return True
    elif plano_socio_torcedor == 3:
         desconto_percentual = valor_ingresso*75/100
         valor_atual = valor_ingresso - desconto_percentual
         print(f'''Você tem acesso ao benefício de 75% de desconto em produtos oficiais.
O novo valor do seu ingresso é de R${valor_atual}''')
         return True
 except:    
    print("Plano sócio-torcedor inválido. Por favor, responda com '1', '2' ou '3'.")
    return False


def forma_pagamento():
    forma_pagamento = int(input("""Qual forma de pagamento você prefere?
1 - Cartão de crédito
2 - Cartão de débito
3 - Pix
: """)).lower()
    
    if forma_pagamento == 1:
        print("Você escolheu pagar com cartão de crédito. Por favor, insira os dados do seu cartão para finalizar a compra.")
        return True
    elif forma_pagamento == 2:
        print("Você escolheu pagar com cartão de débito. Por favor, insira os dados do seu cartão para finalizar a compra.")
        return True
    elif forma_pagamento == 3:
        print("Você escolheu pagar com pix. Por favor, escaneie o código QR para finalizar a compra.")
        return True
    else:
        print("Forma de pagamento inválida. Por favor, responda com '1', '2' ou '3'.")
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
            sair() 
        else:
            print("Opção inválida. Tente novamente.")


def cadastrar():
    while True:
        try:
            nome = input("Digite seu nome completo: ").lower() 
            user = int(input("Digite seu CPF, que será seu usuário: ")) # try: verificar se user já existe 
            senha = input("Digite sua senha: ")
            idade = int(input("Digite sua idade: "))
            if idade < 18:                                   
                print('Você deve ser maior de 18 anos para fazer uma compra.')
                break
            elif idade <= 0:
                print('Idade inválida.')
                break
            else:
                salario = float(input("Digite seu salário atual:"))
                # verificar_salario(salario) == por conta desse verificar_salario, ele tava fazendo o texto aparecer 2 vezes, entao tive que tirar
                if not verificar_salario(salario):   
                    verificar_mensalidade()
                    verificar_plano_socio_torcedor()     
                    print("Cadastro realizado com sucesso!")
                    menu()      
#                  
                usuario = {
                        "nome": nome,
                        "user": user,
                        "idade": idade,
                        "senha": senha,
                        "mensalidade": verificar_mensalidade, #se for 100% deixar vazio
                        "salario": salario,
                        "plano social": verificar_plano_social,
                        "plano sócio-torcedor": verificar_plano_socio_torcedor, #se for 100% deixar vazio
                        "forma de pagamento": forma_pagamento #se for 100% deixar vazio 'retirar um ingresso por mês'?
                }
                
                usuarios.append(usuario)
                print("Cadastro realizado com sucesso!")
                menu() 
        except:
            print('Tente novamete. Algo deu errado.')



def compra():
    if login() == True:
          compra()
    if verificar_plano_social == 3:
        numero_ingresso = random.randint(1000000,1000000)
        print(f'Compra finalizada com sucesso! O número do seu ingresso é {numero_ingresso}.')
    elif verificar_plano_social == 1 or verificar_plano_social == 2:
        print(f'O valor do seu ingressso com desconto é de {verificar_salario(desconto_percentual)}')
        a = int(input('''Deseja finalizar o pagamento?
1 - Sim
2 - Não
: '''))
        if a == 1:
            forma_pagamento()
            numero_ingresso = random.randint(1000000,1000000)
            b = int(input('''Você realizou o pagamento?
1 - Sim
2 - Não
: '''))
            if b == 1:
                print(f'Compra finalizada com sucesso! O número do seu ingresso é {numero_ingresso}.')
        elif a == 2:
            menu()
        

def login():
    user = int(input("Digite seu CPF:"))
    senha = input("Digite sua senha:")
    for usuario in usuarios:
        if usuario["user"] == user and usuario["senha"] == senha:   # <- corrigido () → []
            print("Login bem-sucedido!")
            compra()
            return False
        elif usuario["user"] != user and usuario["senha"] != senha:
            print('Esse usuário não existe')
            return False
        else:    
            print("Usuário ou senha incorretos.")
            return False


while True:
      print(menu())
      
          
         

#antes de finalizar a compra, o sistema irá verificar se o usuário tem direito a algum desconto baseado no salário, plano social e plano sócio-torcedor. O sistema também irá verificar se a mensalidade do usuário está ativa para que ele possa efetivar sua compra.
#observações: questão dos acentos gráficos, o sistema não aceita acentos, então as palavras devem ser digitadas sem acentos para que o sistema funcione corretamente. Exemplo: "sim" ao invés de "sím".
#fazer uma opção no menu para compra