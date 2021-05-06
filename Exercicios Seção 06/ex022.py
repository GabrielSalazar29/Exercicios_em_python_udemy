"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
uma sequência arbitrária de notas (válidas no intervalo de 10 e 20) e morstre na tela,
como resultado, a correspondente média aritmética. O número de notas com que o aluno
pretende efetuar o cálculo não será fornecido ao programa, o qual terminará quando for
um valor que não seja válido como nota de aprovação.
"""


media = soma = x = 0
while True:
    n = float(input("Digite uma nota (entre 10 e 20): "))
    if n > 20 or n < 10:
        break
    else:
        x += 1
        soma += n
        media = soma / x
        print(f"Média = {media:.1f}")
print("FIM!!")
