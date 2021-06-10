"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o
numero do aluno e o segundo representando a sua altura em metros. Encontre o aluno
mais baixo e o mais alto. Mostre o numero do aluno mais baixo e do mais alto, juntamente
com suas alturas.
"""


Numero = []
Altura = []
menor = maior = 0
for i in range(10):
    Numero.append(int(input(f"Digite um numero do aluno {i}: ")))
    Altura.append(float(input(f"Digite a altura do aluno numero {Numero[i]}: ")))
    if i == 0:
        menor = maior = Altura[i]
    elif maior < Altura[i]:
        maior = Altura[i]
    elif menor > Altura[i]:
        menor = Altura[i]


print(f"O numero do aluno mais baixo é {Numero[Altura.index(menor)]}, com {menor}m.\n"
      f"O numero do aluno mais alto é {Numero[Altura.index(maior)]}, com {maior}m.")
