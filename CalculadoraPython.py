print("== CALCULADORA EM PYTHON == \n")

nome = input("Olá, Qual é seu nome ??")
operacao = input(f"Ola {nome}, qual operação deseja executar ? \n \n == + para SOMAR == \n == - para SUBTRAÇÃO == \n == * para MULTIPLICAÇÃO \n == / para DIVISÃO == \n \n")

if operacao == '+':
    y1 = int(input("Digite o primeiro valor ?"))
    y2 = int(input("Digite o segundo valor ?"))
    y3 = y1 + y2
    print(f"{nome} a soma entre {y1} + {y2} é : {y3}")

elif operacao == '-':
    y1 = int(input("Digite o primeiro valor ?"))
    y2 = int(input("Digite o segundo valor ?"))
    y3 = y1 - y2
    print(f"{nome} a subtração entre {y1} - {y2} é : {y3}")

elif operacao == '*':
    y1 = int(input("Digite o primeiro valor ?"))
    y2 = int(input("Digite o segundo valor ?"))
    y3 = y1 * y2
    print(f"{nome} a multiplicação entre {y1} * {y2} é : {y3}")
elif operacao == '/':
    y1 = int(input("Digite o primeiro valor ?"))
    y2 = int(input("Digite o segundo valor ?"))
    y3 = y1 / y2
    print(f"{nome} a divisão entre {y1} / {y2} é : {y3}")

else: print(f"{nome} não localizei a operação desejada, verifique se o SIMBOLO da operação foi digitado corretamente e tente novamente.")
