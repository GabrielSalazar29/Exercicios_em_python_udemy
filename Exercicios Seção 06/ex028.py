"""
Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E,
conforme a fórmula a seguir:
                                E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
"""


n = int(input("Digite um valor: "))

soma = 0
fat = 1
for c in range(n, 0, -1):
    fat = 1
    while True:
        fat *= c
        c -= 1
        if c == 0:
            break
    soma += 1/fat
print(f"{soma:.2f}")
