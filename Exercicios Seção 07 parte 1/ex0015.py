"""
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando ele-
mentos repetidos.
"""


lista = []

for c in range(20):
    lista.append(int(input(f"Digite o numero para a posição {c}: ")))

for c in lista:
    if lista.count(c) == 1:
        print(c)
