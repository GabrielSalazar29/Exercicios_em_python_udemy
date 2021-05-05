"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser
paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:
                -SEM TABELA
"""


venda = float(input("Valor da venda: "))

if venda < 20000:
    Comissão = 400 + (venda * 14 / 100)
elif 20000 <= venda < 40000:
    Comissão = 500 + (venda * 14 / 100)
elif 40000 <= venda < 60000:
    Comissão = 550 + (venda * 14 / 100)
elif 60000 <= venda < 80000:
    Comissão = 600 + (venda * 14 / 100)
elif 80000 <= venda < 100000:
    Comissão = 650 + (venda * 14 / 100)
else:
    Comissão = 700 + (venda * 16 / 100)
print(f"A comissão que deverá ser paga ao vendedor é: {Comissão}")
