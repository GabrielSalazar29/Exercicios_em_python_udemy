"""
Ler dois conjuntos de numeros reais, armazenando-os em vetores e calcular o produto
escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o
produto escalar, sendo que o produto escalar é dado por: x1 * y1 + x2 + y2 +...+ xn * yn.
"""


A = []
B = []
prod = 0
for i in range(5):
    A.append(int(input(f"Digite um numero para o Primeiro conjunto na posição {i}: ")))
    B.append(int(input(f"Digite um numero para o Segundo conjunto na posição {i}: ")))
    prod += A[i] * B[i]
print(f"Conjunto 1 = {A}.\n"
      f"Conjunto 2 = {B}.\n"
      f"Produto escalar = {prod}")
