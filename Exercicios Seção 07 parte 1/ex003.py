"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das
componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm
10 elementos cada. Imprimir todos os conjuntos.
"""


lista1 = [int(i) for i in input("Digite 10 numeros: ").split()]
lista2 = []
for i in lista1:
    lista2.append(i**2)
print(lista1)
print(lista2)
