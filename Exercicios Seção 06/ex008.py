"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor
lido.
"""


maior = menor = 0

for c in range(1, 11):
    x = int(input(f"Digite um numero {c}/10: "))
    if c == 1:
        maior = menor = x
    elif x > maior:
        maior = x
    elif x < menor:
        menor = x
print(f"O maior numero é: {maior}\n"
      f"O menor numero é: {menor}")
