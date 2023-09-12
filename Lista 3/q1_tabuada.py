num = int(input("Digite um número para gerar a tabuada: "))
print(f"\nTabuada de {num}: ")
for i in range(1,11):
    print(f'{num} x {i} = {i*num}')