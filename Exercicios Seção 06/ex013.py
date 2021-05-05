"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números
naturais de 0 até N em ordem crescente.
"""

while True:
    n = int(input("Digite um numero inteiro par: "))
    if n % 2 == 0:
        break
    else:
        print("Digite um numero par!!")

for c in range(0, n+1, 2):
    print(c, end=' ')
