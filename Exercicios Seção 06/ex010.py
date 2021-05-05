"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
"""


n = soma = 0
for c in range(50):
    n += 2
    soma += n
print(f"A soma dos 50 primeiros numeros pares é: {soma}")

