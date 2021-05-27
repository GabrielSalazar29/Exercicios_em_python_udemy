"""
Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encon-
tram o maior e o menor valor.
"""


lista = []

for c in range(5):
    lista.append(int(input(f"Digite o numero para a posição {c}: ")))

print(f"O maior valor está na posição: {lista.index(max(lista))}\n"
      f"O menor valor está na posição: {lista.index(min(lista))}")
