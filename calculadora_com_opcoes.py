# Mostra o menu de opções
print(
    '''
#########################################
        ATENÇÃO USUÁRIO: USE PONTO E NÃO VÍRGULA
        DIGITE 1 PARA SOMAR
        DIGITE 2 PARA SUBTRAIR
        DIGITE 3 PARA MULTIPLICAR
        DIGITE 4 PARA DIVIDIR
########################################
''')

# Pede ao usuário para digitar a opção desejada
print("Digite a função que deseja: ")

# Lê a operação escolhida pelo usuário
operacao = input()

# Verifica a operação escolhida e faz a ação
if operacao == "1":
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    print(x + y)  # Realiza a soma e imprime o resultado

elif operacao == "2":
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    print(x - y)  # Realiza a subtração e imprime o resultado

elif operacao == "3":
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    print(x * y)  # Realiza a multiplicação e imprime o resultado

elif operacao == "4":
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    print(x / y)  # Realiza a divisão e imprime o resultado
