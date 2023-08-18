ganho_por_hora = float(input("Digite quanto você ganha por hora: "))
hora_trabalhada = int(input("Digite quantas horas trabalhadas no mês: "))

salario = ganho_por_hora*hora_trabalhada
imposto_renda = salario*0.11
inss = imposto_renda*0.08
sindicato = inss*0.05
salario_liquido = salario - imposto_renda - inss - sindicato

print(f"\nSalário Bruto: R$ {salario:.2f}")
print(f"IR(11%): R$ {imposto_renda:.2f}")
print(f"INSS(8%): R$ {inss:.2f}")
print(f"Sindicato: R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}\n")