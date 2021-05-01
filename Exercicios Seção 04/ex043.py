"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
    - o total a pagar com desconto de 10%;
    - o valor de cada parcela, no parcelamento de 3x sem juros;
    - a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com des-
    conto)
    - a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""


valor = float(input("Digite o valor total: "))

valor_desconto = valor * 90/100
print(f"O total a pagar com desconto de 10% é: R${valor_desconto:.2f}.\n"
      f"O valor de cada percela, 3x sem juros é: R${valor/3:.2f}.\n"
      f"A comissão do vendedor, se for a vista é: R${valor_desconto * 5/100:.2f}.\n"
      f"A comissão do vendedor, se for parcelada é: R${valor * 5/100:.2f}.")


