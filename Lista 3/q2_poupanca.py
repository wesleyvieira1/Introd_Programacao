deposito_inicial = float(input("Digite o valor do déposito inicial: "))
taxa_juros = float(input("Digite a taxa de juros de uma poupança: "))
deposito = deposito_inicial


for i in range(1,25):
    deposito_inicial+=taxa_juros

    print(f"No {i}º mês: R$ {deposito_inicial}")

print(f"O saldo após 24 meses é de R${deposito_inicial}")
print(f"A taxa de juros foi: R$ {deposito_inicial-deposito}")


