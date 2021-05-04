"""
Calcule as raízes da equação de segundo grau.
A variável 'a' tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não
é equação de segundo grau".
    - Se delta < 0, não existe real. Imprima a mensagem "Não existe raiz".
    - Se delta = 0, existe uma raiz real. Imprima a raiz e a mensagem "Raiz única".
    - Se delta > 0, imprima as duas raízes reais.
"""


a = float(input("Informe o valor de 'a' na equação de segundo grau (ax2 + bx + c = 0):"))
b = float(input("Informe o valor de 'b' na equação de segundo grau (ax2 + bx + c = 0):"))
c = float(input("Informe o valor de 'c' na equação de segundo grau (ax2 + bx + c = 0):"))

delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Não existe raiz")
elif delta == 0:
    raiz = - b / 2 * a
    print(f"Raiz única: {raiz}")
else:
    raiz1 = (- b + (delta ** 0.5)) / 2 * a
    raiz2 = (- b - (delta ** 0.5)) / 2 * a
    print(f"As raizes são {raiz1} e {raiz2}")
