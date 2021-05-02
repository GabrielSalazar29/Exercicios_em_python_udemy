"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso
contrário imprima: Empréstimo concedido.
"""


s = float(input("Digite o salário do trabalhador: "))
emp = float(input("Digite a prestação do empréstimo: "))

if (s * 20 / 100) < emp:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
