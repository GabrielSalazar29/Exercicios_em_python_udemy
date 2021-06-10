"""
Faça um programa que leia um vetor de 10 numeros. Leia um número x. Conte os
multiplos de um número inteiro x num vetor e mostre-os na tela.
"""


vetor = []
for c in range(10):
    vetor.append(float(input(f"Digite o numero da posição {c}: ")))

x = int(input("Digite um numero: "))

for c in vetor:
    if c % x == 0:
        print(f"Multiplo de {x}: {c}")
