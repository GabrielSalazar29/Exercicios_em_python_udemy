"""
Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12,
e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28
dias em anos não bissextos.
"""


dia = int(input("Digite um dia: "))
mes = int(input("Digite um numero correspondente ao mes: "))
ano = int(input("Digite um ano: "))

if ano % 400 == 0 or (ano % 4 == 0 and not ano % 100 == 0):
    ano_b = 'bissexto'
else:
    ano_b = 'não bissexto'

if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias = 30
elif mes == 2:
    if ano_b == 'bissexto':
        dias = 29
    else:
        dias = 28
elif 0 < mes <= 12:
    dias = 31

if 0 < dia <= dias:
    print("Válido")
else:
    print("Inválido")
