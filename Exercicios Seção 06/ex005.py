"""
Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""


soma = 0
for c in range(1, 11):
    x = int(input(f"Digite o inteiro {c}/10: "))
    soma += x
print(f"A soma é: {soma}")
