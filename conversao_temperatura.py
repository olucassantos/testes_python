# Programa para fazer conversão de temperaturas

# Celsius para Farenheit: celsius * 1.8 + 32
# Celsius para Kelvin: celsius + 273

print("============================================")
print("============== CONVERSOR 5000 ==============")
print("============================================")

celsius = float(input("Digite a temperatura em Celsius: "))

farenh = celsius * 1.8 + 32
kelvin = celsius + 273

print(f"A temperatura em Farenheit é: {farenh}")
print(f"A temperatura em Kelvin é: {kelvin}")