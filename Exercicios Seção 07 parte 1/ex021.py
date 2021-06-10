"""
Faça um programa que receba do usuario dois vetores, A e B, com 10 numeros inteiros
cada. Crie um novo vetor denominado C calculando C = A - B. Mostre na tela os dados
do vetor C.
"""


A = []
B = []
C = []
for i in range(10):
    A.append(int(input(f"Digite um numero para o Primeiro vetor na posição {i}: ")))
    B.append(int(input(f"Digite um numero para o Segundo vetor na posição {i}: ")))
    C.append(A[i] - B[i])

print(C)
