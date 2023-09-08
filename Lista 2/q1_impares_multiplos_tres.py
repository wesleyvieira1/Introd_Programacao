contador = 1
soma = 0

while contador <= 500:
    if contador%2==1 and contador%3==0:
        soma+=contador
    contador+=1
    
print(f"A soma é: {soma}")
