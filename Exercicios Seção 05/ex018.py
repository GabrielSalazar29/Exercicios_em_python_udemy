"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações ma-
temáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu pro-
grama então pede dois valores numéricos e realiza a operação, mostrando o resultado e
saindo.
"""


op = int(input("Escolha a operação que deseja.\n"
               "Digite 1 para somar.\n"
               "Digite 2 para subtrair.\n"
               "Digite 3 para multiplicar.\n"
               "Digite 4 para dividir: "))

x = float(input("Digite um numero: "))
y = float(input("Digite outro numero: "))

if op == 1:
    resultado = x + y
elif op == 2:
    resultado = x - y
elif op == 3:
    resultado = x * y
elif op == 4:
    resultado = x / y
else:
    resultado = 0
    print("Operação não encontrada. Logo...")
print(f"O resultado é: {resultado}")
