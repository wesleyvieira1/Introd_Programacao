numero = menor = maior = int(input("Digite um número [-1 para sair]: "))
contador = 0
while numero!=-1:
    contador+=numero
    if numero>maior:
        maior = numero
    if numero<menor:
        menor = numero
    numero = int(input("Digite um número [-1 para sair]: "))

print(f"\nO maior número foi: {maior}")
print(f"O menor número foi: {menor}")
print(f"A soma dos números digitados foi: {contador}")