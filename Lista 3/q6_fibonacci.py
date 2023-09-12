n = int(input("Digie quantos termos na sequência de fibonacci você quer: "))

if n<=1:
    print(n)
else:
    primeiro, segundo = 1, 1
    print(primeiro)
    print(segundo)

    for i in range(2, n):
        proximo = primeiro + segundo
        print(proximo)
        primeiro, segundo = segundo, proximo


