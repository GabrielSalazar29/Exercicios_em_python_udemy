"""
Faça um programa para ler as dimensões de um terreno (comprimento 'c' e largura 'l'),
bem como o preço do metro de tela 'p'. Imprima o custo para cercar esse mesmo terreno
com tela.
"""


c = float(input("Digite o comprimento do terreno: "))
l = float(input("Digite a largura do terreno: "))
p = float(input("Digite o preço do metro de tela: "))

perimetro = (c * 2) + (l * 2)
custo = perimetro * p
print(f"O custo para cercar esse terreno é: R${custo:.2f}")
