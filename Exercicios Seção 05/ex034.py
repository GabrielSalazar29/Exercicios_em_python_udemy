"""
Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.
"""


nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Quantas faltas? "))

if 0 <= nota < 4:
    if faltas <= 20:
        conceito = 'E'
    else:
        conceito = 'E'
elif nota < 5:
    if faltas <= 20:
        conceito = 'D'
    else:
        conceito = 'E'
elif nota < 7.5:
    if faltas <= 20:
        conceito = 'C'
    else:
        conceito = 'D'
elif nota < 9:
    if faltas <= 20:
        conceito = 'B'
    else:
        conceito = 'C'
elif nota <= 10:
    if faltas <= 20:
        conceito = 'A'
    else:
        conceito = 'B'
print(f"Conceito do aluno: {conceito}")
