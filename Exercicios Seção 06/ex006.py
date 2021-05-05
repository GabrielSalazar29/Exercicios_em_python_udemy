"""
Faça um programa que leia 10 inteiros e imprima sua média.
"""


soma = 0
for c in range(1, 11):
    x = int(input(f"Digite o inteiro {c}/10: "))
    soma += x
media = soma / 10
print(f"A média é: {media}")
