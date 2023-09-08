num1 = int(input("Digite o divisor: "))
num2 = int(input("Digite o dividendo: "))

numero1 = num1

subtracao = 0

while num1>=num2:
    subtracao+=1
    num1-=num2

print(f'\nA divisão de {numero1} / {num2} = {subtracao} com resto = {num1}')
print(f'Podemos subtrair {num2} "{subtracao}" vezes de {numero1}')