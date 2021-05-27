"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
e imprima a média geral.
"""


notas = []

for c in range(15):
    notas.append(float(input(f"Digite a nora do aluno numero {c+1}: ")))

media = sum(notas)/len(notas)

print(f"A media geral é: {media}")
