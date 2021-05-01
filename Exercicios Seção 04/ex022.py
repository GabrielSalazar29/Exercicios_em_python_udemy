"""
Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula
de conversão é: M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento
em metros.
"""


cj = float(input("Digite um comprimento em jardas: "))
cm = 0.91 * cj
print(f"O valor digitado em metros é: {cm:.2f}m")
