"""
Leia um valor de área em acres e apresente-o convertido em metros quadrados. A
fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A
a área em acres.
"""


aa = float(input("Digite uma área em acres: "))
am = aa * 4048.58
print(f"A área digitada em metros quadrados é:{am} m2")
