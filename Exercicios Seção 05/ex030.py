"""
Faça um programa que receba três números e mostre-os em ordem crescente.
"""


x = float(input("Digite um numero: "))
y = float(input("Digite outro numero: "))
z = float(input("Digite mais um numero: "))

if x > y > z:
    print(f"Os números em ordem crescente são: {z} -> {y} -> {x}")
elif x > z > y:
    print(f"Os números em ordem crescente são: {y} -> {z} -> {x}")
elif z > x > y:
    print(f"Os números em ordem crescente são: {y} -> {x} -> {z}")
elif z > y > x:
    print(f"Os números em ordem crescente são: {x} -> {y} -> {z}")
elif y > x > z:
    print(f"Os números em ordem crescente são: {z} -> {x} -> {y}")
else:
    print(f"Os números em ordem crescente são: {x} -> {z} -> {y}")
