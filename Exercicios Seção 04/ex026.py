"""
Leia um valor de área em metros quadrados e apresente-o convertido em hectares.
A fórmula de conversão é:H = M * 0.0001, sendo M a área em metros quadrados e H
a área em hectares.
"""


am = float(input("Digite uma área em metros quadrados: "))
ah = am * 0.0001
print(f"A área digitada em hectares é: {ah} ha")
