n = int(input("Digite um número para obter a raiz quadrada: "))
b = 2
p = (b+n/b)/2

while abs(b-p)>0.0001:
    b = p
    p = (b+(n/b))/2

print(f"A raiz quadrada de {n} é {b:.2f}")