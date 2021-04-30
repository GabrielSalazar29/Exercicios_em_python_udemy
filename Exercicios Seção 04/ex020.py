"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fómula
de conversão é: L = K/0.45, sendo K a massa em quilogramas e L a massa em libras.
"""


mk = float(input("Digite um peso em quilogramas: "))
ml = mk / 0.45
print(f"O peso informado convertido em Libras é: {ml:.2f}lb")
