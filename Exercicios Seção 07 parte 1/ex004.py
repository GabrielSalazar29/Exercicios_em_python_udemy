"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois va-
lores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa
deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.
"""


lista = []
soma = 0

for c in range(8):
    lista.append(int(input(f"Digite o numero para a posição {c}: ")))

x = int(input("Digite a posição X: "))
y = int(input("Digite a posição Y: "))

for i, c in enumerate(lista):
    if i == x or i == y:
        soma += c

print(f"A soma dos numeros nas posições solicitadas é {soma}")
