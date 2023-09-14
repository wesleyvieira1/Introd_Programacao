base = soma = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

for i in range(0,expoente-1):
    soma*=base

print(f"{base} elevado {expoente} = {soma}")