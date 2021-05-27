"""
Fazer um programa para ler 5 valores e, um seguida, mostrar todos os valores lidos
juntamente com o maior, o menor e a média dos valores.
"""

lista = []

for c in range(5):
    lista.append(int(input(f"Digite o numero para a posição {c}: ")))

print(f"Os valores digitados foram: {lista}\n"
      f"O maior valor digitado foi: {max(lista)}\n"
      f"O menor valor digitado foi: {min(lista)}\n"
      f"A media dos valores é: {sum(lista)/5}")
