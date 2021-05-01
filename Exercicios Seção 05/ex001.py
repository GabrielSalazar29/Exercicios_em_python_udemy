"""
Faça um programa que receba dois números e mostre qual deles é o maior.
"""


n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

if n1 > n2:
    maior = n1
else:
    maior = n2

print(f"O maior numero é o {maior}")
