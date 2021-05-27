"""
Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a
quantidade de números negativos e a soma dos números positivos desse vetor.
"""


lista = []
cont_n = 0
soma_p = 0
for c in range(10):
    lista.append(int(input(f"Digite o numero para a posição {c}: ")))

for c in lista:
    if c < 0:
        cont_n += 1
    else:
        soma_p += c

print(f"O numero de negativos é: {cont_n}\n"
      f"A soma dos positivos é: {soma_p}")
