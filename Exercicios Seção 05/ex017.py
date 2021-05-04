"""
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
    A = (B + b) * h / 2
Lembre-se, a base maior e a base menor devem ser números maiores que zero.
"""


B = float(input("Informe a Base maior do trapézio: "))
b = float(input("Informe a Base menor do trapézio: "))
h = float(input("Informe a altura do trapézio: "))

A = (B + b) * h / 2

print(f"A área do trapézio é: {A}")
