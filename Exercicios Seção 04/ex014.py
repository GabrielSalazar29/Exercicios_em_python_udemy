"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * π/180, sendo G o ângulo em graus e R em radianos e π = 3.14.
"""


ag = float(input("Digite um ângulo em graus: "))
ar = ag * 3.14/180
print(f"O ângulo digitado em radianos é: {ar}")
