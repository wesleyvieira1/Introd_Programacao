nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))

media = (nota_um+nota_dois)/2
print(media)
if 9.0 <= media <= 10.0:
    print("Parabéns! Sua média foi A")

elif 7.5 <= media <= 9.0:
    print("Ótimo! Sua média foi B")

elif 6.5 <= media <= 7.5:
    print("Boa! Sua média foi C")

elif 4.0 <= media <= 6.0:
    print("Estude mais! Sua média foi D")

else:
    print("Reprovado! Sua média foi E")