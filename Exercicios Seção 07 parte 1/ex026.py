"""
Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 numeros,
onde m é a media do vetor.
"""


from math import sqrt

v = []
soma = 0

for i in range(10):
    v.append(float(input(f"Digite o numero da posição {i}: ")))
    soma += v[i]
m = soma / len(v)
DP = 0

for i in v:
    DP += (i - m) ** 2

DP = sqrt(DP / len(v))

print(f"O desvio padrão é: {DP:.4f}")
