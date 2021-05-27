"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima
o vetor, o maior elemento e a posição que ele se encontra.
"""


lista = []

for c in range(10):
    lista.append(int(input(f"Digite o numero para a posição {c}: ")))

print(f"O vetor é: {lista}\n"
      f"O maior elemento é: {max(lista)}\n"
      f"A posição que ele se encontra é {lista.index(max(lista))}")

