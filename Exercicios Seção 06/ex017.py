"""
Faça um programa que leia um número inteiro positivo "n" e calcule a soma dos "n" primeiros
números naturais.
"""


n = int(input("Digite um numero inteiro : "))
soma = 0
for c in range(n):
    soma += c
print(soma)
