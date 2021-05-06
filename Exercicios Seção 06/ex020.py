"""
Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá
ser informado o número de dados lidos e número de valores pares. O processo termina
quando for digitado o número 1000.
"""

x = 0
par = 0
x_total = 0
while x != 1000:
    x = int(input("Digite um numero (para sair digite 1000): "))
    x_total += 1
    if x % 2 == 0:
        par += 1
print(f"Foram lidos {x_total} numeros, e desses numeros, {par} são pares.")
