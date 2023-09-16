# 1.  Verificação de idade
# Crie um programa que peça ao usuário para inserir sua idade e, em
# seguida, informe se a pessoa é menor de idade ou maior de idade.

# - Solicitar a idade do usuário
# - Decidir se idade é maior ou menor que 18

print("============================================")
print("============== DETRAM IDADE S ==============")
print("============================================")

idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Você não passa de um bebe")
else:
    print("Você é maior de idade")