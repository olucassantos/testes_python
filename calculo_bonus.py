# 4. Cálculo de Bônus Salarial
# Peça ao usuário para inserir seu salário e o tempo de serviço. 
# Se o tempo de serviço
# for superior a 5 anos, conceda um bônus de 5% ao salário.

# - Solicitar salário
# - Solicitar tempo de serviço
# - Decidir se vai aplicar o bonus
# - Mostrar resultado

salario = float(input("Digite seu salário: "))
tempo_servico = float(input("Informe o tempo de serviço: "))

total = 0
if tempo_servico > 5:
    total = salario * 1.05
else:
    total = salario

if (total > salario):
    print(f"Seu novo salário é de {total}")
else:
    print(f"Seu salário permance o mesmo.")