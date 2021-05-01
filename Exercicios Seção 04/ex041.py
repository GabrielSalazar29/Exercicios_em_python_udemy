"""
Faça um programa que leia o valor da hora de trabalho (em reais) e números de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado.
"""


ht = float(input("Digite o valor da hora de trabalho (em reais): "))
nh = float(input("Digite o número de horas trabalhadas no mês: "))

vp = ht * nh * 110/100

print(f"O valor a ser pago ao funcionário é: R${vp:.2f}")
