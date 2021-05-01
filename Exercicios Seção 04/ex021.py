"""
Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fómula
de conversão é:K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""


ml = float(input("Digite um peso em libras: "))
mk = ml * 0.45
print(f"O peso informado convertido em quilogramas é: {mk:.2f}kg")
