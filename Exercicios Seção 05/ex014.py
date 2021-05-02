"""
A nota final de um estudante é calculada a partir de três notas atribuidas entre o intevalo
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral
e a um exame final. A média das três notas mencionadas anteriormente obedece aos
pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9), de
recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.
"""


n1 = float(input("Quanto o aluno tirou no trabalho de laboratório (de 0 a 10): "))
n2 = float(input("Quanto o aluno tirou na avaliação semestral (de 0 a 10): "))
n3 = float(input("Quanto o aluno tirou no exame final (de 0 a 10): "))

nota1 = n1 * 2 / 10
nota2 = n2 * 3 / 10
nota3 = n3 * 5 / 10
media = (nota1 + nota2 + nota3)
print(f"A média do aluno foi {media:.1f}")
if media <= 2.9:
    situação = "reprovado"
elif media <= 4.9:
    situação = "recuperação"
else:
    situação = "aprovado"
print(f"situação do aluno: {situação}")
