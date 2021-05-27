"""
Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores
lidos na ordem inversa.
"""


lista = []

while len(lista) < 6:

    x = int(input("Digite um numero par: "))
    if x % 2 == 0:
        lista.append(x)
    else:
        print("\033[31mDigite um numero par!\033[m")
lista.reverse()
print("Os valores na ordem inversa são: ")
for c in lista:
    print(c)
