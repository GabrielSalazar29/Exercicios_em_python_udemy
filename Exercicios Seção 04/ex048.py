"""
Leia um valor inteiro em segundos, e imprima em horas, minutos e segundos.
"""


s = int(input("Digite um valor inteiro em segundos: "))

horas = s / 3600
sr = s % 3600
minutos = sr / 60
segundos = sr % 60

print(f"Esse valor da {int(horas)} horas/{int(minutos)} minutos/{segundos} segundos.")
