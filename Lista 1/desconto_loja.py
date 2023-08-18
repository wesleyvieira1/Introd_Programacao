produto = float(input("Digite o valor gasto na Loja: "))
forma_pagamento = str(input("""
                            
        Digite DIN - Dinheiro
        Digite CH - Cheque
        Digite CA - Cartão\n
        Qual a forma de pagamento? """)).upper()

if produto>=100 and forma_pagamento=="DIN":
    desconto = produto - (produto*0.1)
    print(f"\nVocê teve desconto!! O valor da compra ficou: R$ {desconto}")

elif forma_pagamento=="CA":
    print("\nForma de pagamento inválida")

else:
    print(f"\nSua compra ficou R$ {produto}")
    
