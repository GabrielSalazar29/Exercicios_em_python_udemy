"""
Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuirem
valores negativos.
"""


vetor = []
for c in range(10):
    x = float(input(f"Digite o numero da posição {c}: "))
    if x > 0:
        vetor.append(x)
    else:
        x = 0
        vetor.append(x)
print(vetor)
