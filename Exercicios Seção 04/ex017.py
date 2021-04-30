"""
Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C/2.54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""


cc = float(input("Digite um comprimento em centímetros: "))
cp = cc/2.54
print(f"O comprimento digitado em polegadas é: {cp:.2f}in")