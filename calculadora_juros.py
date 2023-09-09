# Programa para calcular o juros

print("============================================")
print("============== JUROS PRO 1000 ==============")
print("============================================")

valor_inicial = float(input("Digite o valor inicial: "))
taxa_anual = float(input("Digite a taxa anual em porcentagem: "))
tempo_anos = float(input("Digite o tempo em anos: "))

montante = valor_inicial + (valor_inicial * (taxa_anual / 100) * tempo_anos)

print(f"O valor total será de: {montante}")