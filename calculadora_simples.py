# 2.  Calculadora Simples
# Peça ao usuário para inserir dois números e uma operação (+, -, *, /).
# Realize a operação e exiba o resultado.

# - Solicitar primeiro numero
# - Solicitar segundo numero
# - Solicitar uma operacao
# - Decidir qual operacao executar
# - Realizar a operacao

numero_um = float(input("Digite o primeiro numero: "))
numero_dois = float(input("Digite o segundo numero: "))
operacao = input("Selecione a operação que deseja realizar (+ - * /): ")

resultado = ''
if operacao == '+':
    resultado = numero_um + numero_dois
elif operacao == '-':
    resultado = numero_um - numero_dois
elif operacao == '*':
    resultado = numero_um * numero_dois
elif operacao == '/':
    if numero_dois == 0:
        print("Não é possivel dividir por zero")
    else:
        resultado = numero_um / numero_dois
else:
    print("Operação não reconhecida.")

if resultado != '':
    print(f"O resultado é: {resultado}")