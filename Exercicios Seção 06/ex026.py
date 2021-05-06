"""
Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número
dado.
"""


x = int(input("Digite um número: "))
while True:
    if x % 11 == 0 or x % 13 == 0 or x % 17 == 0:
        break
    else:
        x += 1
print(x)
