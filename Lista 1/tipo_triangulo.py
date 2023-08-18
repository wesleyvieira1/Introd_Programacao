lado_um = float(input("Digite um valor para um triângulo: "))
lado_dois = float(input("Digite um valor para um triângulo: "))
lado_tres = float(input("Digite um valor para um triângulo: "))

if lado_um==lado_dois==lado_tres:
    print("Triângulo Equilátero")
elif lado_um==lado_dois or lado_dois==lado_tres:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")