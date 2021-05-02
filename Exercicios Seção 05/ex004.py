"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    - O número digitado ao quadrado
    - A raiz quadrada do número digitado
"""


x = float(input("Digite um numero: "))

if x > 0:
    print(f"O número digitado ao quadrado é {x**2}\n"
          f"A raiz quadrada do número digitado é {x**0.5}")
