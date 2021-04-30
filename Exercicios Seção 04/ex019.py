"""
Leia um valor de volume em litros e apresente-o convertido em metros cúbicos. A
fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em
metros cúbicos.
"""

vl = float(input("Digite um valor em Litros: "))
vm = vl/1000
print(f"O valor digitado em metros cúbicos é: {vm}m3")
