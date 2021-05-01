"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro-
porcionalmente ao valor que cada um deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um
ganharia do prêmio com base no valor investido.
"""


v1 = float(input("Digite quanto o primeiro amigo investiu: "))
v2 = float(input("Digite quanto o segundo amigo investiu: "))
v3 = float(input("Digite quanto o terceiro amigo investiu: "))

soma = v1 + v2 + v3

vr1 = v1 * 100 / soma
vr2 = v2 * 100 / soma
vr3 = v3 * 100 / soma

print(f"A porcentagem do valor que cada um reberá respectivamente é {vr1}%, {vr2}% e {vr3}%")
