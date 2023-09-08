x = 70.000
y = 180.000
ano = 0

while (x<=y):
    x *= 0.035 + 1 #1 ano
    y *= 0.015 + 1 #1 ano
    
    ano+=1

print(f"Precisará de {ano} ano(s)")
