"""
Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""


x = int(input("Digite um numero: "))

for c in range(1, x + 1):
    if x % c == 0:
        print(c)
