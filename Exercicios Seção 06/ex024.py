"""
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores
desse número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é
1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""


x = int(input("Digite um numero: "))

soma = 0
for c in range(1, x):
    if x % c == 0:
        soma += c

print(f"A soma dos divisores é {soma}")
