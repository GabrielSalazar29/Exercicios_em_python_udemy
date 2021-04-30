"""
Leia um valor de volume em metros cúbicos e apresente-o convertido em litros. A
fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em
metros cúbicos.
"""

vm = float(input("Digite um valor em metros cúbicos: "))
vl = 1000 * vm
print(f"O valor digitado em Litros é: {vl}L")
