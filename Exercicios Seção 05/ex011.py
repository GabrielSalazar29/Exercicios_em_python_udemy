"""
Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela a
soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá ao valor
8 = (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a
mensagem "Número inválido".
"""


x = int(input("Digite um numero inteiro: "))
soma = 0
if x > 0:
    for i in str(x):
        soma = soma + int(i)
    print(f"A soma de todos os algarismos desse número é {soma}")
else:
    print("Número inválido")
