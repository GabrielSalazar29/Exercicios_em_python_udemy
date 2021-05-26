"""
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""


lista = []
cont = 0
for c in range(10):
    lista.append(int(input(f"Digite o numero para a posição {c}: ")))

for c in lista:
    if c % 2 == 0:
        cont += 1

print(f"A quantidade de numeros pares é {cont}")
