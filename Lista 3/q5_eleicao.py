eleitores = int(input("Digite o número de eleitores: "))


lula = 0
bolsonaro = 0
ciro = 0
nulo = 0

for i in range (0, eleitores):
    print('''
          
        Vote:
          [12] - Ciro
          [13] - Lula
          [17] - Bolsonaro
          [0] - Nulo

    ''')
    voto = int(input("Seu voto é: "))
    while voto!=12 and voto!=13 and voto!=17 and voto!=0:
        print("Voto Inválido!")
        voto = int(input("Seu voto é: "))

    if voto==12:
        ciro+=1
    elif voto==13:
        lula+=1
    elif voto==17:
        bolsonaro+=1
    else:
        nulo+=1

print(f"\nCiro recebeu {ciro} voto(s)")
print(f'Lula recebeu {lula} voto(s)')
print(f"Bolsonaro recebeu {bolsonaro} voto(s)")
print(f"Houve {nulo} voto(s) nulo(s)")