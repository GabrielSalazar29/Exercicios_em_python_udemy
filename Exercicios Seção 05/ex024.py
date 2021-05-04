"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS
8%). Faça um programa em que o usuário entre com o valor e o estado destino do
produto e o programa retorne o preço final do produto acrescido do imposto do estado
em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem
de erro.
"""


valor = float(input("Informe o valor do produto: "))
destino = str(input("Informe o destino do produto: ")).strip().upper()

if destino == 'MG':
    print(f"O valor do produto ficou = {valor * 107 / 100}")
elif destino == 'SP':
    print(f"O valor do produto ficou = {valor * 112 / 100}")
elif destino == 'RJ':
    print(f"O valor do produto ficou = {valor * 115 / 100}")
elif destino == 'MS':
    print(f"O valor do produto ficou = {valor * 108 / 100}")
else:
    print("Erro, estado inválido!!!")
