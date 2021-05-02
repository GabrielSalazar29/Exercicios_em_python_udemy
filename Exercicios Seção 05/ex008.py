"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um
valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser
informado ao usuário e o programa termina.
"""


n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite outra nota: "))

if 0 <= n1 <= 10  and 0 <= n2 <= 10:
    media = (n1 + n2) / 2
    print(f"A média desse aluno é : {media}")
else:
    print("As notas não possuem um valor válido!")
