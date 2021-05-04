"""
Escrever um programa que leia o código do produto escolhido do cardápio de uma lan-
chonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido. O cardápio da lan-
chonete segue o padrão abaixo:
                ___________________________________
                | Especificação  | Código|  Preço |
                -----------------------------------
                | Cachorro Quente|  100  |  1.20  |
                | Bauru Simples  |  101  |  1.30  |
                | Bauru com Ovo  |  102  |  1.50  |
                | Hamburguer     |  103  |  1.20  |
                | Cheeseburguer  |  104  |  1.70  |
                | Suco           |  105  |  2.20  |
                | Refrigerante   |  106  |  1.00  |
                -----------------------------------
"""


codigo = int(input("Digite o código do produto que deseja: "))
quanti = int(input("Digite a quantidade: "))

if codigo == 100:
    preço = 1.20
elif codigo == 101:
    preço = 1.30
elif codigo == 102:
    preço = 1.50
elif codigo == 103:
    preço = 1.20
elif codigo == 104:
    preço = 1.70
elif codigo == 105:
    preço = 2.20
elif codigo == 106:
    preço = 1.00
print(f"O valor total a ser pago é: R${(quanti * preço):.2f}")
