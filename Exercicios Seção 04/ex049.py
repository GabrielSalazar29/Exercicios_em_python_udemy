"""
Faça um programa que leia o horário (hora, minuto e segundo) de inicio e duração, em
segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora,minutos e segundos) do termino da mesma.
"""


hi = int(input("Digite a hora que começou a experiencia: "))
mi = int(input("Digite os minutos: "))
si = int(input("Digite e os segundos : "))
td = int(input("Digite o tempo de duração em segundos : "))

horas = td / 3600
sr = td % 3600
minutos = sr / 60
segundos = sr % 60

hf = hi + horas
mf = mi + minutos
sf = si + segundos

segundos_finais = sf % 60
mff = mf + (segundos_finais / 60)
minutos_finais = mff % 60
horas_finais = hf + (mff // 60)

print(f"A hora do termino da experiência é: {int(horas_finais)}:{int(minutos_finais)}:{int(segundos_finais)}")
