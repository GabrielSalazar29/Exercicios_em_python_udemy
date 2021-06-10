"""
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo,
nas posições pares os valores do primeiro e nas posições impares os valores do se-
gundo.
"""


A = []
B = []
C = []
for i in range(10):
    A.append(int(input(f"Digite um numero para o Primeiro vetor na posição {i}: ")))
    B.append(int(input(f"Digite um numero para o Segundo vetor na posição {i}: ")))
    if i % 2 == 0:
        C.append(A[i])
    else:
        C.append(B[i])

print(C)