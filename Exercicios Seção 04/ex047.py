"""
Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito po linha.
"""


x = int(input("Digite um numero inteiro com 4 digitos: "))

sx = str(x)

print(f"{sx[0]}\n"
      f"{sx[1]}\n"
      f"{sx[2]}\n"
      f"{sx[3]}")
