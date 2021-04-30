"""
Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R * 180/π, sendo G o ângulo em graus e R em radianos e π = 3.14.
"""


ar = float(input("Digite um ângulo em radianos: "))
ag = ar * 180/3.14
print(f"O ângulo digitado em graus é: {ag}")
