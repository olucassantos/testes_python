# 3. Classificação de Notas
# Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como
# "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).

# - Solicitar nota ao usuário
# - Decidir a Nota

nota = float(input("Digite o resultado (0 - 100): "))

if nota < 60:
    print("F")
elif nota <= 69 and nota >= 60:
    print("D")
elif nota <= 79 and nota >= 70:
    print("C")
elif nota <= 89 and nota >= 80:
    print("B")
elif nota >= 90 and nota <= 100:
    print("A")
else:
    print("Sua nota máxima é 100")