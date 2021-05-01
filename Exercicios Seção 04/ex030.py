"""
Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente
em dólares.
"""


vr = float(input("Digite o valor em real:"))
cd = float(input("Digite a cotação do dolar: "))

vd = vr / cd
print(f"este valor em dólar é: U${vd:.2f}")
