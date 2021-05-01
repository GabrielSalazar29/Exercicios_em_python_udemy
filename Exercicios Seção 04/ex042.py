"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-
se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base.
"""


sb = float(input("Informe o salário-base do funcionário: "))

grat = sb * 5/100
imp = sb * 7/100
sfinal = sb + grat - imp

print(f"O salário final é: R${sfinal:.2f}")
