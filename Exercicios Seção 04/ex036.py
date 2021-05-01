"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio da seguinte fórmula: V = π * raio**2 * altura,
onde π = 3.141592.
"""


a = float(input("Digite a altura do cilindro: "))
r = float(input("Digite o raio do cilindro: "))

v = 3.141592 * r**2 * a
print(f"O volume do cilindro circular é : {v:.2f}")
