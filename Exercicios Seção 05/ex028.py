"""
Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:
    - Geométrica
    - Ponderada
    - Harmônica
    - Aritimética
"""


x = int(input("Digite um numero inteiro: "))
y = int(input("Digite outro numero inteiro: "))
z = int(input("Digite mais um numero inteiro: "))
resp = int(input("Digite 1 para calcular a média geométrica.\n"
                 "Digite 2 para calcular a média ponderada.\n"
                 "Digite 3 para calcular a média harmônica.\n"
                 "Digite 4 para calcular a média aritimética.\n"
                 "Opção:"))

if resp == 1:
    media = (x * y * z) ** (1/3)
elif resp == 2:
    media = (x + 2 * y + 3 * z) / 6
elif resp == 3:
    media = 1 / (1/x + 1/y + 1/z)
elif resp == 4:
    media = (x + y + z) / 3
else:
    media = 0
    print("Opção não encontrada!!!")
print(f"Média = {media:.2f}")
