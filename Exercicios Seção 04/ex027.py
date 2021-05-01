"""
Leia um valor de área em hectares e apresente-o convertido em metros quadrados.
A fórmula de conversão é:M = H * 10000, sendo M a área em metros quadrados e H
a área em hectares.
"""


ah = float(input("Digite uma área em hectares: "))
am = ah * 10000
print(f"A área digitada em metros quadrados é: {am} m2")