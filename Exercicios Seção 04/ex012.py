"""
Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de
conversão é: K = 1.61 * M, sendo K a distância em quilômetros e M em milhas.
"""


dm = float(input("Digite uma distância em milhas: "))
dk = 1.61 * dm
print(f"Essa distância convertida em km fica: {dk:.2f}km")
