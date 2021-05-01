"""
Sejam 'a' e 'b' os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raiz(a**2 + b**2). Faça um programa que receba os valores de 'a' e 'b' e calcule
o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
"""


a = float(input("Digite o primeiro cateto: "))
b = float(input("Digite o segundo cateto: "))

hipotenusa = (a**2 + b**2)**0.5
print(f"O valor da hipotenusa é {hipotenusa}")
