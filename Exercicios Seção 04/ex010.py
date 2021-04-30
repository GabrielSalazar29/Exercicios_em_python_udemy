"""
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
km/h e M em m/s.
"""
vk = float(input("Digite uma velocidade em km/h: "))
vm = vk / 3.6
print(f"A velocidade convertida para m/s ficou dessa forma: {vm:.2f}m/s")
