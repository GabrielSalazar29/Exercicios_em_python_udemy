"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo.
"""


ad = float(input("Informe a altura dos degraus da escada: "))
al = float(input("Informe a altura que quer alcançar: "))

nd = al / ad
print(f"Você deverá subir {nd} degraus para atingir seu objetivo.")
