"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondendo a este numero. Isto é, domingo se 1, segunda-feira se 2, e
assim por diante.
"""


dia = int(input("Digite um numero correspondente ao dia da semana: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
else:
    print("Sabado")
