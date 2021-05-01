"""
Leia um valor de área em metros quadrados e apresente-o convertido em acres. A
fórmula de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e A
a área em acres.
"""


am = float(input("Digite uma área em metros quadrados: "))
aa = am * 0.000247
print(f"A área digitada em acres é:{aa}ac")
