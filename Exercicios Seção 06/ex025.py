"""
Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos
de 3 ou 5.
"""


soma = 0
for c in range(1, 1000):
    if c % 3 == 0 or c % 5 == 0:
        soma += c
print(f"A soma dos numeros é :{soma}")
