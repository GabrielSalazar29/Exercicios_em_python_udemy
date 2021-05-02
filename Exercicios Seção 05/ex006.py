"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""


n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

print(f"O maior numero é o {maior} e a diferença entre o maior numero e o menor é : {maior - menor}")
