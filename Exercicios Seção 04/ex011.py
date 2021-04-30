"""
Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilômetros por hora). A fórmula de conversão é: K = M*3.6, sendo K a velocidade
em km/h e M em m/s.
"""
vm = float(input("Digite uma velocidade em m/s: "))
vk = vm*3.6
print(f"A velocidade convertida para km/h ficou dessa forma: {vk:.2f}km/h")

