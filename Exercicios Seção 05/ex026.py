"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com
a tabela abaixo:
                      _____________________________________
                      | CONSUMO | (Km/l) |   MENSAGEM     |
                      |menor que|   8    |  Venda o carro!|
                      |entre    | 8 e 14 |      Econômico!|
                      |maior que|  12    |Super econômico!|
                      -------------------------------------
"""


dist = float(input("Quantos Km é o percurso? "))
cons = float(input("Quantos L de gasolina foi consumido? "))

km_l = dist / cons

if km_l < 8:
    print("Venda o carro!")
elif 8 < km_l < 14:
    print("Econômico!")
else:
    print("Super econômico")
