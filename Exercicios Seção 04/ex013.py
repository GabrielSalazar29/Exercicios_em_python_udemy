"""
Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de
conversão é: M = K/1.61, sendo K a distância em quilômetros e M em milhas.
"""


dk = float(input("Digite uma distância em quilômetros: "))
dm = dk/1.61
print(f"Essa distância convertida em mi fica: {dm:.2f}mi")
