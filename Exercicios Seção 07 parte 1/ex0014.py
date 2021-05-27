"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais
e os escreva na tela.
"""


lista = []

for c in range(10):
    lista.append(int(input(f"Digite o numero para a posição {c}: ")))

for c in lista:
    if lista.count(c) > 1:
        print(c)
