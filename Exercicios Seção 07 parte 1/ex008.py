"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos
na ordem inversa.
"""


lista = []

for c in range(6):
    lista.append(int(input(f"Digite o numero para a posição {c}: ")))
lista.reverse()
print(f"Os valores na ordem inversa é: {lista}")
