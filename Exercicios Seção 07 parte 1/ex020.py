"""
Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um
vetor com 10 posições. preencha um segundo vetor apenas com os números ímpares
do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.
"""


vetortemp = []
vetor = []
for c in range(50):
    vetortemp.append(c)
    if len(vetortemp) == 5:
        vetor.append(vetortemp.copy())
        vetortemp.clear()

vetorimpar = []
for c in vetor:
    for n in c:
        if n % 2 != 0:
            vetorimpar.append(n)
print(vetor)
print(vetorimpar)
