"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas( onde h corresponde à altura):
    - Homens: (72.7 * h) -58
    - Mulheres: (62.1 * h) - 44.7
"""


h = float(input("Digite sua altura: "))
s = str(input("Digite seu sexo (H/M): ")).strip().upper()[0]

if s == 'H':
    peso_ideal = (72.7 * h) - 58
else:
    peso_ideal = (62.1 * h) - 44.7

print(f"Seu peso ideal é {peso_ideal:.2f}")
