n = int(input("Digite o número de pessoas para verificar a idade: "))
turma = 0

for i in range(1,n+1):
    print(f"Digite a {i}º idade: ", end="")
    idade = int(input())

    turma+=idade

media = turma/n

if 0 < media <= 25:
    print("A turma é jovem")

elif 26 < media <= 60:
    print("A turma é adulta")

else:
    print("A turma é idosa")