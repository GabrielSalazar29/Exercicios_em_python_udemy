"""
Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira
vez deve usar a estrutura de repetição 'for', a segunda 'while', e a terceira "do while".
"""


for c in range(1, 101):
    print(c)
x = 1
while x < 101:
    print(x)
    x += 1
y = 1
while True:
    print(y)
    y += 1
    if y == 101:
        break
