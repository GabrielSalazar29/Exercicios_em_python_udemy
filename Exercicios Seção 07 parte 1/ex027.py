"""
Leia 10 numeros inteiros e armazene em um vetor. Em seguida escreva os elementos
que são primos e suas respectivas posições no vetor
"""


vetor = []

for i in range(10):
    vetor.append(int(input(f"Digite o numero para aposição {i}: ")))

div = []
for k, i in enumerate(vetor):
    for c in range(1, i+1):
        if i % c == 0:
            div.append(c)
    if len(div) == 2:
        print(f"O numero {i} é primo e está na posição {k}")
    div.clear()
