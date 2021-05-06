"""
Faça um programa que receba dois números. Calcule e mostre:
    - a soma dos números pares desse intervalo de números, incluindo os números digi-
      tados;
    - a multiplicação dos números ímpares desse intervalo, incluindo os digitados;
"""


x = int(input("Digite um valor: "))
y = int(input("Digite outro valor: "))
soma = 0
multi = 1
for c in range(x, y+1):
    if c % 2 == 0:
        soma += c
    else:
        multi *= c
print(f"A soma dos numeros pares é {soma}.\n"
      f"A multiplicação dos numeros impares é {multi}.")
