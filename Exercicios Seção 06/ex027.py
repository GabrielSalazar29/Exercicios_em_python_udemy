"""
Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma
da série harmonica:
                        H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor "n" inteiro e positivo e apresente o valor de H(n).
"""


n = int(input("Digite um valor: "))

soma = 0
for c in range(1, n + 1):
    soma += 1/c
print(f"O valor de H(n) é : {soma:.2f}")
