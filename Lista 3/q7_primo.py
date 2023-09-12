n = int(input("Digite um número: "))

primo = True
if n==1:
    print("Não é primo")
else:
    for i in range (2,n):
        if n%i==0:
            primo = False

    if primo:
        print(f"O número {n} é primo")

    else:
        print(f"O número {n} não é primo")