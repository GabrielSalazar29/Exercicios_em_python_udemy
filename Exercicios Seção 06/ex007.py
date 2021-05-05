"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
média.
"""


soma = 0
i = 0
for c in range(1, 11):
    x = int(input(f"Digite um inteiro positivo {c}/10: "))
    if x > 0:
        i += 1
        soma += x
media = soma / i
print(f"A média é: {media}")
