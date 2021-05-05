"""
Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída
cada um dos algarismos que compõem o número
"""


while True:
    x = int(input("Digite um número inteiro entre 100 e 999: "))
    if not 100 <= x <= 999:
        print("Erro!! Resposta inválida.")
    else:
        break
for i, c in enumerate(str(x)):
    print(f"O algarismo numero {i+1} é: {c}")
