"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o
número é invalido.
"""


x = int(input("Digite um numero qualquer: "))

if x > 0:
    print(f"A raiz quadrada desse número é : {x ** 0.5}")
else:
    print("Número invalido")
