turno = str(input("""\n
    Digite M - Matutino
    Digite V - Vespertino 
    Digite N - Noturno\n
    Qual turno você estuda?: """)).upper()

if turno=="M":
    print("\nBom Dia!")
elif turno=="V":
    print("\nBoa Tarde!")
elif turno=="N":
    print("\nBoa Noite!")
else:
    print("Valor Inválido!!")