"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostra qual a classificação dessa pessoa.
"""


altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))

if altura < 1.20:
    if peso < 60:
        classificação = 'A'
    elif peso <= 90:
        classificação = 'D'
    else:
        classificação = 'G'
elif altura <= 1.70:
    if peso < 60:
        classificação = 'B'
    elif peso <= 90:
        classificação = 'E'
    else:
        classificação = 'H'
else:
    if peso < 60:
        classificação = 'C'
    elif peso <= 90:
        classificação = 'F'
    else:
        classificação = 'I'
print(f"A classificação é: {classificação}")
