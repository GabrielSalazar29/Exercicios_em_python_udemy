"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação esco-
lhida. Escreva uma mensagem de erro se a opção for inválida.

Escolha a opção:
1-Soma de 2 números.
2-Diferença entre 2 números (maior pelo menor).
3-Produto entre 2 números.
4-Divisão entre 2 números (o denominador não pode ser zero).
Opção
"""


op = int(input("Escolha a opção.\n"
               "1-Soma de 2 números.\n"
               "2-Diferença entre 2 números (maior pelo menor).\n"
               "3-Produto entre 2 números.\n"
               "4-Divisão entre 2 números (o denominador não pode ser zero).\n"
               "Opção: "))

x = float(input("Digite um numero: "))
y = float(input("Digite outro numero: "))

if op == 1:
    resultado = x + y
elif op == 2:
    resultado = x - y
elif op == 3:
    resultado = x * y
elif op == 4:
    resultado = x / y
else:
    resultado = 0
    print("Operação não encontrada. Logo...")
print(f"O resultado é: {resultado}")
