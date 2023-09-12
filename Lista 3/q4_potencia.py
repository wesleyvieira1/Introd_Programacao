base = int(input("Digite um valor para base: "))
expoente = int(input("Digite um valor para o expoente: "))



for i in range(1, expoente+1):
    potencia = i * expoente

print(f"{base} elevado a {expoente} é {potencia}")

