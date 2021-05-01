"""
Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o número ao quadrado.
"""


x = float(input("Digite um número qualquer: "))

if x > 0:
    print(f"A raiz quadrada desse número é : {x ** 0.5}")
else:
    print(f"Esse número ao quadrado é: {x ** 2}")
