# Uma loja oferece pagamentos por Pix, á vista ou por cartão de crédito. Os clientes que pagam atraves de boleto tem direito a 5% de desconto sobre o valor da compra, enquanto os clientes que pagam á vista tem ate 8% de desconto com compras a partir de R$200.00, enquanto os clientes que pagam no cartão de crédito podem escolher parcelar até 12x.
print("Saldão das ofertas!")

total_compra = float(input("Por favor, informe o valor total da compra do cliente:\n"))
forma_pagamento = int(input("Selecione a forma de pagamento: 1 - Pix, 2 - Á vista ou 3 - Cartão de credito:\n"))

if forma_pagamento == 1:
# 5% de desconto no pix para compras a partir R$100
    if total_compra >= 100:
        total_compra_desconto = total_compra * 0.95
    else:
        total_compra_desconto = total_compra

    print(
          f"O valor total da compra foi de R$ {total_compra:.2f}"
          f" teve um desconto pelo pagamento via pix."
          f" O cliente deverá pagar R$ {total_compra_desconto:.2f}."
    )

elif forma_pagamento == 2:
#8% de desconto para compras a partir de R$200
    if total_compra >= 200:
        total_compra_desconto = total_compra * 0.92
    else:
        total_compra_desconto = total_compra

    print(
        f"O valor total da compra foi de R$ {total_compra:.2f}"
          f" teve um desconto pelo pagamento á vista."
          f" O cliente deverá pagar R$ {total_compra_desconto:.2f}."
    )

elif forma_pagamento == 3:
# parcelamento
    parcelas = int(input("Informe a quantidade de parcelas desejadas:\n"))
    valor_parcelas = total_compra / parcelas
    print(f"O total da compra de R$ {total_compra:.2f}"
      f" será pago em {parcelas} parcelas de R$ {valor_parcelas:.2f}."
      )
