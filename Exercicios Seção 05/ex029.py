"""
Faça uma prova de matemática para crianças que estão aprendendo a somar números
inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, mostre na
tela a pergunta: qual é a soma de  a + b, onde a e b são os números aleatórios. Peça a
resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou.
"""


from random import randint

acertos = 0
for c in range(0, 5):
    a = randint(1, 100)
    b = randint(1, 100)
    print(f"Qual o resultado de {a} + {b}?")
    resp = int(input("Resposta: "))
    if a + b == resp:
        acertos = acertos + 1
print(f"Você acertou {acertos} questões")
