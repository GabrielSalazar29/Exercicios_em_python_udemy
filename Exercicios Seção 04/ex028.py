"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos
três valores lidos.
"""


n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))
n3 = float(input("Digite mais um valor: "))

soma = (n1**2) + (n2**2) + (n3**2)
print(f"A soma de {n1**2} + {n2**2} + {n3**2} = {soma}")
