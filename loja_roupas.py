# Objetivo - Calcular o valor final da venda de produtos

# A vista:
## 10% de desconto
## 15% de desconto em compras acima 500
## 20% acima de 1000

# A prazo:
## Parcelamento acima de 5x em compras acima de 800
## Parcelamento em até 18x
## Juros, caso mais de 10x

import os
import sys
# os.system('cls')

print("============================================")
print("================ LOJA ROUPAS ===============")
print("============================================")

print("Programa para auxiliar ao calculo de vendas de produtos")

# 1 - Solicitar o valor total dos produtos
valor_produtos = float(input("Informe o total em produtos: "))

# 2 - Solicitar a forma de pagamento
forma_pagamento = input("Qual a forma de pagamento? (1 vista, 2 prazo)")


valor_final = 0
# 3 - Decidir como calcular o valor final a partir da forma de pagamento
if forma_pagamento == '1': # pagamento a vista
    # 3.1.1 - Aplicar desconto de 10%
    valor_final = valor_produtos - valor_produtos * 0.1
    # 3.1.2 - Aplicar desconto de 5% caso seja maior que 500
    valor_final -= valor_produtos * 0.05 if valor_produtos > 500 else 0
    # 3.1.3 - Aplicar desconto de 5% caso seja maior que 1000
    valor_final -= valor_produtos * 0.05 if valor_produtos > 1000 else 0

elif forma_pagamento == '2': # pagamento a prazo
    # 4 - Mostrar resumo da compra

    # 3.2.1 - Mostrar a quantidade de parcelas possiveis
    max_parcelas = "18" if valor_produtos > 800 else '5'
    print(f"Você pode parcelar em até {max_parcelas} vezes.")

    quantidade_parcelas = int(input("Em quantas vezes deseja fazer o parcelamento?\n"))

    if(valor_produtos < 800 and quantidade_parcelas > 5 or quantidade_parcelas < 2):
        print("Quantidade não permitida.")
        sys.exit()
        possui_erro = True
    elif(quantidade_parcelas > 18):
        print("Quantidade não permitida.")
        possui_erro = True
    else:
        possui_erro = False
        if (quantidade_parcelas > 10):
            # 3.2.2 - Aplicar juros, caso seja maior que 10 parcelas
            if quantidade_parcelas == 11: juros = 0.05
            elif quantidade_parcelas == 12: juros = 0.065 
            elif quantidade_parcelas == 13: juros = 0.07 
            elif quantidade_parcelas == 14: juros = 0.09 
            elif quantidade_parcelas == 15: juros = 0.095 
            elif quantidade_parcelas == 16: juros = 0.1 
            elif quantidade_parcelas == 17: juros = 0.113 
            elif quantidade_parcelas == 18: juros = 0.12

            valor_final = valor_produtos + valor_produtos * (juros * quantidade_parcelas)
        else:
            valor_final = valor_produtos
        
        valor_parcela = valor_final / quantidade_parcelas
else:
    print("Forma de pagamento inválida!")

# Resumo

if not possui_erro:
    if (forma_pagamento == '1'):
        print(f"O valor total da compra é de {valor_final}")
        print("Total de desconto: %.2f" % (valor_produtos - valor_final))
    else:
        print("O valor total da compra é de %.2f" % valor_final)
        print("Será pago em %i de %.2f" % (quantidade_parcelas, valor_parcela))

print("Obrigado!")