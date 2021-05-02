"""
Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem 'Números iguais'.
"""


n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

if n1 > n2:
    print(f"O maior numero é o {n1}")
elif n2 > n1:
    print(f"O maior numero é o {n2}")
else:
    print(f"Números iguais")
