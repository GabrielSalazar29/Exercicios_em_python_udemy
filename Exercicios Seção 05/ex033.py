"""
Um produto vai sofrer aumento de acordo com a tabela a baixo. Leia o preço antigo,
calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de
acordo com a segunda tabela).
"""


preço = float(input("Digite o preço para ser atualizado: "))

if preço < 50:
    preço_novo = preço * 105 / 100
elif preço <= 100:
    preço_novo = preço * 110 / 100
else:
    preço_novo = preço * 115 / 100
print(f"O preço novo é {preço_novo}")
if preço_novo < 80:
    print("Barato")
elif preço_novo <= 120:
    print("Normal")
elif preço_novo <= 200:
    print("Caro")
else:
    print("Muito caro")
