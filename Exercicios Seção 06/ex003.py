"""
Faça um algoritimo utilizando o comando while que mostra uma contagem regressiva
na tela, iniciando em 10 e terminando em 0. Mostrar uma mensagem "FIM!" após a
contagem.
"""


c = 10
while True:
    print(c)
    c -= 1
    if c < 0:
        break
print("FIM!")
