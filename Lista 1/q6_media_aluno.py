nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))

media = (nota_um+nota_dois)/2
#print(media)

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media <= 9.0:
    conceito = "B"
elif 6.5 <= media <= 7.5:
    conceito = "C"
elif 4.0 <= media <= 6.0:
    conceito = "D"
else:
    conceito = "E"

print(f"O conceito da média do aluno foi {conceito}")