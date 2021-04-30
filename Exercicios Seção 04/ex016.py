"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""


cp = float(input("Digite um comprimento em polegadas: "))
cc = cp * 2.54
print(f"O comprimento digitado em centímetros é: {cc}cm")
