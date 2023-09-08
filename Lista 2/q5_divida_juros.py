
valor_divida = float(input("Digite o valor inical da dívida: "))
juro_mensal = float(input("Digite o valor do juro mensal: "))
valor_mensal = float(input("Digite o valor mensal que será pago: "))

meses = 0
total_juros = 0
total_pago = valor_divida

while valor_mensal<=valor_divida:

    juros = valor_divida * (juro_mensal/100)
    valor_divida += juros-valor_mensal
    total_juros += juros
    meses+=1

total_pago += total_juros

print(f"\nA dívida será paga em {meses} mes(es)")
print(f"O total pago foi R$ {total_pago:.2f}")
print(f"O total de juros pagos foi R$ {total_juros:.2f}")

