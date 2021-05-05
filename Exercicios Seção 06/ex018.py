"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e
quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser
fornecida pelo usuário.
"""


quant = int(input("Quantos numeros voçê deseja que sejam lidos? "))
maior = 0
lista = []
for c in range(quant):
    n = float(input("Digite um numero: "))
    lista.append(n)
    if n > maior:
        maior = n
print(f"O maior numero é {maior} e ele aparece {lista.count(maior)} vez.")
