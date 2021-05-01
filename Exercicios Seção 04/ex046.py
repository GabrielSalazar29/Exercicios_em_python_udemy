"""
Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do numero lido. Exemplo: NúmeroLido = 123
NúmeroGerado = 321.
"""


x = int(input("Digite um numero de 3 digitos inteiro: "))
sx = str(x)
print(f"O numero invertido fica: {sx[::-1]}")
