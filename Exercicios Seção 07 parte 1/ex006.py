"""
Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá
ser impresso o maior e o menor elemento do vetor.
"""


lista = []

for c in range(10):
    lista.append(int(input(f"Digite o numero para a posição {c}: ")))

print(f"O maior valor digitado é {max(lista)}\nO menor valor digitado é {min(lista)}")
