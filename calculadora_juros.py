# Programa para calcular o juros
import os

print("============================================")
print("============== JUROS PRO 1000 ==============")
print("============================================")

valor_inicial = float(input("Digite o valor inicial: "))
taxa_anual = float(input("Digite a taxa anual em porcentagem: "))
tempo_anos = float(input("Digite o tempo em anos: "))

montante = valor_inicial + (valor_inicial * (taxa_anual / 100) * tempo_anos)

os.system('cls' if os.name == 'nt' else 'clear')

print(f"O valor total será de: {montante}")