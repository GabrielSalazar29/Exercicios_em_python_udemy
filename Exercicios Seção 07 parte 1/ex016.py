"""
Faça um programa que leia um vetor de 5 posições para números reais e, depois, um
código inteiro. Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem
direta; se for 2, mostre o vetor na ordem inversa. Caso, o código for diferente de 1 e 2
escreva uma mensagem informando que o código é inválido.
"""

vetor = []
for c in range(5):
    vetor.append(float(input(f"Digite o numero da posição {c}: ")))
while True:
    print("=" * 20)
    op = int(input("Digite 0 para sair.\n"
                   "Digite 1 para mostrar o vetor na ordem direta.\n"
                   "Digite 2 para mostrar o vetor na ordem inversa.\n"
                   "OPÇÃO: "))
    print("=" * 20)
    if op == 0:
        print("Encerrando...")
        break
    elif op == 1:
        vetor.sort()
        print(vetor)
    elif op == 2:
        vetor.reverse()
        print(vetor)
    else:
        print("O código é inválido")
