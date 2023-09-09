# Programa para calcular o IMC

print("============================================")
print("============= CALCULO IMC 3000 =============")
print("============================================")

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura * altura)

print("============================================")

print(f"Olá {nome};")
print(f"Sua idade é de {idade} anos;")
print(f"Seu IMC é de {imc};")