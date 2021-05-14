"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
"""


lista = []
for c in range(1, 7):
    lista.append(int(input(f"Digite um {c}/6 numero: ")))
print(f"{lista[0]} {lista[1]} {lista[2]} {lista[3]} {lista[4]} {lista[5]}")
