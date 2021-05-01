"""
A quantia de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia principal:
    - O primeiro ganhador receberá 46%;
    - O segundo receberá 32%;;
    - o terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""


j1 = 780_000 * 46/100
j2 = 780_000 * 32/100
j3 = 780_000 - (j1 + j2)
print(f"O primeiro ganhador recebeu : R${j1:.2f}\n"
      f"O segundo ganhador recebeu : R${j2:.2f}\n"
      f"O terceiro ganhador recebeu : R${j3:.2f}")
