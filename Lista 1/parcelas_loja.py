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
    funcao = str(input("""
                            
        Digite D - Débito
        Digite C - Crédito\n
        Qual o tipo do cartão? """)).upper()
    
    if funcao=="D":
        print(f"\nSua compra ficou R$ {produto}")

    else:
        parcelas = int(input("\nVocê pode parcelar em até 3 parcelas.\nQuantas vai querer? "))
        if parcelas==1:
            print(f"\nSua compra ficou R$ {produto}")
        elif parcelas==2:
            produto_parcelado = produto/2
            print(f"\nSua compra ficou R$ {produto} com 2 parcelas de R$ {produto_parcelado}")
        elif parcelas==3:
            produto_parcelado = produto/3
            print(f"\nSua compra ficou R$ {produto} com 2 parcelas de R$ {produto_parcelado}")
        else:
            print("\nQuantidades de parcelas inválida!")
else:
    print(f"\nSua compra ficou R$ {produto}")
    
