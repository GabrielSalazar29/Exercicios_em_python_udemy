"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para impostos de renda.
"""


dias = int(input("Quantos dias esse trabalhador vai trabalhar? "))

vl = dias * 30 * 92/100

print(f"O valor líquido que ele receberá é : R${vl:.2f}")
