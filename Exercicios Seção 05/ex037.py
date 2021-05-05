"""
As tarifas de certo parque de estacionamento são as seguintes:
    - 1 e 2 horas - R$1.00 cada
    - 3 e 4 horas - R$1.40 cada
    - 5 horas e seguintes - R$2.00 cada
O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida
deste são apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12 50 representará "dez para uma da tarde". Pretende-se criar um
programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela
o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com
intervalo não superior a 24 horas. Portando, se uma dada hora de chegada for superior
à de partida, isso não é uma situação de erro, antes significará que a partida ocorreu no
dia seguinte ao da chegada.
"""


hora_c = int(input("Informe a hora de chegada: "))
min_c = int(input("Informe os minutos: "))
hora_p = int(input("Informe a hora da partida: "))
min_p = int(input("Informe os minutos: "))

min_chegada_tot = hora_c * 60 + min_c
min_partida_tot = hora_p * 60 + min_p
if min_chegada_tot <  min_partida_tot:
    min_permanencia = min_partida_tot - min_chegada_tot
else:
    min_permanencia = (24 * 60 - min_chegada_tot) + min_partida_tot

if 0 < (min_permanencia / 60) <= 2:
    tarifa = 1
elif (min_permanencia / 60) <= 4:
    tarifa = 1.40
else:
    tarifa = 2
print(f"O total a se pagar é R${(min_permanencia / 60) * tarifa:.2f}")
