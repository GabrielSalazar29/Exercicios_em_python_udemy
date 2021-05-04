"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:
    - Infantil A: 5 a 7 anos
    - Infantil B: 8 a 10 anos
    - Juvenil A: 11 a 13 anos
    - Juvenil B: 14 a 17 anos
    - Sênior: maiores de 18 anos
"""


idade = int(input("Digite a idade do nadador: "))

if 5 <= idade <= 7:
    print("Infantil A")
elif 8 <= idade <= 10:
    print("Infantil B")
elif 11 <= idade <= 13:
    print("Juvenil A")
elif 14 <= idade <= 17:
    print("Juvenil B")
else:
    print("Sênior")
