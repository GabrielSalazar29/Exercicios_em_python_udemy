"""
Faça um programa para verificar se um determinado número inteiro é divisivel por 3 ou
5, mas não simultaneamente pelos dois.
"""


n = int(input("Digite um numero inteiro: "))

if (n % 3 == 0 or n % 5 == 0) and not (n % 3 == 0 and n % 5 == 0):
    print("Esse numero é divisivel por 3 ou por 5 mas não pelos 2 simultaneamente")
else:
    print("O numero não é divisivel por nenhum dos 2, ou é divisivel pelos 2 simultaneamente")
