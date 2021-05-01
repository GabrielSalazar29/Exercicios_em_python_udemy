"""
Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule sua
distâcia da origem(0,0).
"""


x = float(input("Informe em que ponto do eixo x o ponto se encontra: "))
y = float(input("Informe em que ponto do eixo y o ponto se encontra: "))

d = ((x**2) + (y**2)) ** 0.5
print(f"A distancia desse ponto para a origem é : {d:.2f}")
