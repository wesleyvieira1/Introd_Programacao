altura = float(input("Digite sua altura: "))
genero = int(input("Você é homem ou mulher?\n Digite 1 - Mulher\n Digite 2 - Homem:  "))

if genero==1:
    peso = (72.7*altura) - 58
    print(f"Seu peso ideal é {peso:.2f}")
if genero==2:
    peso = (61.1*altura) - 44.7
    print(f"Seu peso ideal é {peso:.2f}")
else:
    print("Digitou o número errado!!")

