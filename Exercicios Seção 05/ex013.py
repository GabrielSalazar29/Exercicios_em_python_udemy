"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e
a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 60 pontos.
"""


n1 = float(input("Quanto o aluno tirou na primeira prova (de 0 a 100): "))
n2 = float(input("Quanto o aluno tirou na segunda prova (de 0 a 100): "))
n3 = float(input("Quanto o aluno tirou na terceira prova (de 0 a 100): "))

nota1 = n1 * 25 / 100
nota2 = n2 * 25 / 100
nota3 = n3 * 50 / 100
media = (nota1 + nota2 + nota3)
print(f"A média do aluno foi {media}")
if media >= 60:
    situação = "aprovado"
else:
    situação = "reprovado"
print(f"O aluno está {situação}")
