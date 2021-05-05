"""
Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números
naturais de 1 até N em ordem decrescente.
"""

while True:
    n = int(input("Digite um numero inteiro ímpar: "))
    if n % 2 != 0:
        break
    else:
        print("Digite um numero ímpar!!")

for c in range(n, 0, -2):
    print(c, end=' ')
