"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguin-
tes conceitos:
    - O comprimento de cada lado de um triângulo é menor do que a soma dos outros
    dois lados
    - Chama-se equilátero o triângulo que tem três lados iguais.
    - Denominam-se isósceles o triângulo que tem o comprimento de dois
    -Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""


r1 = float(input("Fale uma reta: "))
r2 = float(input("Fale outra reta: "))
r3 = float(input("Fale outra reta: "))
if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    print("Essas retas podem formar um triangulo")
else:
    print("Essas retas não podem formar um triangulo")
print("\033[33m=-\033[m"*20)
if r1 == r2 and r2 == r3:
    print("É um triangulo equilatero, pois todos os lados são iguais")
elif r1 == r2 or r2 == r3 or r1 == r3:
    print("É um triangulo isosceles, pois apenas 2 lados são iguais")
else:
    print("É um triangulo escaleno, pois todos os lados são diferentes")
