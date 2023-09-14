soma = base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

resultado = 1

if expoente < 0:
    expoente = -(expoente)
    for i in range(expoente):
            resultado *= soma
    print(f"{base} elevado a {expoente} = {1/resultado}")
else:
    for i in range(expoente):
        resultado *= soma

    print(f"{base} elevado a {expoente} = {resultado}")