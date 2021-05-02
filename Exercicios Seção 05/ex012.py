"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número
inválido". Se o número for positivo, calcular o logaritmo deste numero.
"""


from math import log10

x = int(input("Digite um numero inteiro: "))

if x > 0:
    log = log10(x)
    print(f"O log de {x} é {log}")
else:
    print("Número inválido")
