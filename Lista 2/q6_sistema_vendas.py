codigo = int(input("Digite o valor do código: "))
compra = 0


while codigo!=0:

    if codigo==1:
        compra+=5.50
    elif codigo==2:
        compra+=2.30
    elif codigo==3:
        compra+=4.75
    elif codigo==5:
        compra+=9.30
    else:
        print("Código inválido")

    codigo = int(input("Digite o valor do código: "))

print(f"A sua compra deu R$ {compra:.2f}")